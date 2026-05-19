
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

model = SentenceTransformer(
    "sentence-transformers/paraphrase-MiniLM-L3-v2"
)

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

def generate_embeddings(chunk_texts):

    embeddings = model.encode(
        chunk_texts,
        show_progress_bar=True
    )

    return embeddings
