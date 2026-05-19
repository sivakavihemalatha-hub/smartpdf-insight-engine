
# ==========================================
# embedding_generator.py
# ==========================================

# PURPOSE:
# Generate semantic embeddings from document chunks
# using SentenceTransformer model.

# ==========================================
# IMPORT REQUIRED LIBRARIES
# ==========================================

from sentence_transformers import SentenceTransformer

# ==========================================
# LOAD EMBEDDING MODEL
# ==========================================
# This model converts text into semantic vectors.


# ==========================================
# LOAD MODEL ONLY ONCE
# ==========================================

_embedding_model = None

def get_embedding_model():

    global _embedding_model

    if _embedding_model is None:

        _embedding_model = SentenceTransformer(
            "sentence-transformers/paraphrase-MiniLM-L3-v2",
            device="cpu"
        )

    return _embedding_model


# ==========================================
# FUNCTION:
# generate_embeddings()
# ==========================================
# INPUT:
# List of chunk texts
#
# OUTPUT:
# Numerical vector embeddings
# ==========================================

def generate_embeddings(chunk_texts, model):

    embeddings = model.encode(
        chunk_texts,
        show_progress_bar=False
    )

    return embeddings
