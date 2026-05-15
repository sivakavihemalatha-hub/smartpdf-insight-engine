
# ==========================================
# rag_engine.py
# ==========================================

# PURPOSE:
# Generate intelligent answers using:
# - Retrieved chunks
# - Groq LLM
# - RAG prompting

# ==========================================
# IMPORT REQUIRED LIBRARIES
# ==========================================

import os

from groq import Groq

# ==========================================
# INITIALIZE GROQ CLIENT
# ==========================================

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ==========================================
# FUNCTION:
# generate_rag_answer()
# ==========================================
# PURPOSE:
# Generate final answer from retrieved chunks
#
# INPUT:
# question
# retrieved_chunks
#
# OUTPUT:
# Final AI-generated answer
# ==========================================

def generate_rag_answer(

    question,
    retrieved_chunks
):

    # ======================================
    # STEP 1 — COMBINE RETRIEVED CHUNKS
    # ======================================

    context = "\n\n".join(
        retrieved_chunks
    )

    # ======================================
    # STEP 2 — CREATE RAG PROMPT
    # ======================================

    prompt = f"""
You are an advanced AI Document Intelligence System.

Answer the user's question ONLY using the provided document context.

If the answer is not available in the context,
reply with:

"Answer not found in document."

========================================
DOCUMENT CONTEXT:
========================================

{context}

========================================
USER QUESTION:
========================================

{question}

========================================
FINAL ANSWER:
========================================
"""

    # ======================================
    # STEP 3 — GENERATE LLM RESPONSE
    # ======================================

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are a document question answering system."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.2
    )

    # ======================================
    # STEP 4 — EXTRACT FINAL ANSWER
    # ======================================

    final_answer = response.choices[0].message.content

    # ======================================
    # STEP 5 — RETURN ANSWER
    # ======================================

    return final_answer
