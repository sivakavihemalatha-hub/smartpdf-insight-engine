
# ==========================================
# retriever.py
# ==========================================

# PURPOSE:
# Retrieve most relevant chunks from FAISS
# using semantic similarity search.

# ==========================================
# IMPORT REQUIRED LIBRARIES
# ==========================================

import numpy as np

# ==========================================
# FUNCTION:
# retrieve_chunks()
# ==========================================
# PURPOSE:
# Convert user question into embedding,
# search FAISS index,
# retrieve top matching chunks.
#
# INPUT:
# question
# embedding_model
# faiss_index
# chunk_store
# top_k
#
# OUTPUT:
# Retrieved chunk texts
# ==========================================

def retrieve_chunks(

    question,
    embedding_model,
    faiss_index,
    chunk_store,
    top_k=3
):

    # ======================================
    # STEP 1 — CREATE QUESTION EMBEDDING
    # ======================================

    question_embedding = embedding_model.encode(
        [question]
    )

    question_embedding = np.array(
        question_embedding,
        dtype=np.float32
    )

    # ======================================
    # STEP 2 — SEARCH FAISS INDEX
    # ======================================

    distances, indices = faiss_index.search(
        question_embedding,
        top_k
    )

    # ======================================
    # STEP 3 — RETRIEVE MATCHING CHUNKS
    # ======================================

    retrieved_chunks = []

    for chunk_index in indices[0]:

        chunk_data = chunk_store[chunk_index]

        retrieved_chunks.append(
            chunk_data["chunk_text"]
        )

    # ======================================
    # STEP 4 — RETURN RETRIEVED CHUNKS
    # ======================================

    return retrieved_chunks
