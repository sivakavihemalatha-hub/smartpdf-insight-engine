import os
import json
from sentence_transformers import SentenceTransformer

from utils.validator import validate_pdf
from utils.pdf_extractor import extract_pdf_content
from utils.cleaner import clean_text
from utils.chunker import chunk_text
from utils.embedding_generator import generate_embeddings
from utils.faiss_manager import create_faiss_index, save_faiss_index, load_faiss_index
from utils.summarizer import summarize_text
from utils.retriever import retrieve_chunks
from utils.rag_engine import generate_rag_answer

# ==========================================
# GLOBAL MODEL (LOAD ONCE)
# ==========================================

#embedding_model = SentenceTransformer(
   # "sentence-transformers/all-MiniLM-L6-v2"
#)

_embedding_model = None

def get_embedding_model():
    global _embedding_model

    if _embedding_model is None:
        from sentence_transformers import SentenceTransformer

        _embedding_model = SentenceTransformer(
            "sentence-transformers/paraphrase-MiniLM-L3-v2",
            device="cpu"
        )

    return _embedding_model

BASE_PATH = "documents"


# ==========================================
# SUMMARY PIPELINE
# ==========================================

def process_document(file_path):

    is_valid, msg = validate_pdf(file_path)
    if not is_valid:
        return {"status": "error", "message": msg}

    doc_name = os.path.splitext(os.path.basename(file_path))[0]
    document_id = doc_name.replace(" ", "_")

    folder = os.path.join(BASE_PATH, document_id)
    os.makedirs(folder, exist_ok=True)

    text = clean_text(extract_pdf_content(file_path))

    chunks = chunk_text(text)

    chunk_store = [
        {"chunk_id": i, "chunk_text": c}
        for i, c in enumerate(chunks)
    ]

    chunks_path = os.path.join(folder, "chunks.json")

    with open(chunks_path, "w", encoding="utf-8") as f:
        json.dump(chunk_store, f, indent=4)

    texts = [c["chunk_text"] for c in chunk_store]

    batch_size = 16
    embeddings = []

    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        batch_embeddings = generate_embeddings(batch, get_embedding_model())
        embeddings.extend(batch_embeddings.tolist())

    index = create_faiss_index(embeddings)

    faiss_path = os.path.join(folder, "index.faiss")
    save_faiss_index(index, faiss_path)

    chunk_summaries = [summarize_text(t) for t in texts]
    final_summary = summarize_text("\n\n".join(chunk_summaries))

    summary_path = os.path.join(folder, "summary.json")

    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump({
            "document_id": document_id,
            "summary": final_summary
        }, f, indent=4)

    return {
        "status": "success",
        "document_id": document_id,
        "summary": final_summary,
        "chunks_path": chunks_path,
        "faiss_path": faiss_path,
        "summary_path": summary_path
    }


# ==========================================
# QA PIPELINE
# ==========================================

def ask_document_question(question, document_id):

    chunks_path = os.path.join(BASE_PATH, document_id, "chunks.json")

    with open(chunks_path, "r", encoding="utf-8") as f:
        chunk_store = json.load(f)

    index = load_faiss_index(
        os.path.join(BASE_PATH, document_id, "index.faiss")
    )

    retrieved = retrieve_chunks(
        question,
        get_embedding_model(),
        index,
        chunk_store,
        top_k=3
    )

    return generate_rag_answer(question, retrieved)
