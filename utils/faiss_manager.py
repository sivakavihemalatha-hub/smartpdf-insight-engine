
# ==========================================
# faiss_manager.py
# ==========================================

# PURPOSE:
# Handle FAISS vector database operations:
# - Create FAISS index
# - Store embeddings
# - Save FAISS index
# - Load FAISS index

# ==========================================
# IMPORT REQUIRED LIBRARIES
# ==========================================

import faiss
import numpy as np

# ==========================================
# FUNCTION:
# create_faiss_index()
# ==========================================
# PURPOSE:
# Convert embeddings into FAISS vector database
#
# INPUT:
# embeddings
#
# OUTPUT:
# FAISS index
# ==========================================

def create_faiss_index(embeddings):

    # Convert embeddings into NumPy array
    embedding_array = np.array(
        embeddings,
        dtype=np.float32
    )

    # Get embedding dimension
    dimension = embedding_array.shape[1]

    # Create FAISS index
    index = faiss.IndexFlatL2(dimension)

    # Store embeddings in FAISS
    index.add(embedding_array)

    return index

# ==========================================
# FUNCTION:
# save_faiss_index()
# ==========================================
# PURPOSE:
# Save FAISS index into Google Drive
#
# INPUT:
# index
# save_path
# ==========================================

def save_faiss_index(index, save_path):

    faiss.write_index(index, save_path)

# ==========================================
# FUNCTION:
# load_faiss_index()
# ==========================================
# PURPOSE:
# Load stored FAISS index
#
# INPUT:
# faiss_path
#
# OUTPUT:
# Loaded FAISS index
# ==========================================

def load_faiss_index(faiss_path):

    index = faiss.read_index(faiss_path)

    return index
