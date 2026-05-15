
# ==========================================
# summarizer.py (MODULE ONLY - STORE IN DRIVE)
# ==========================================

import os
from groq import Groq

# GROQ CLIENT (AI ENGINE)
# :contentReference[oaicite:0]{index=0}

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# ==========================================
# PROMPT BUILDER
# ==========================================

def create_summary_prompt(text):

    prompt = f"""
You are an advanced AI Document Intelligence System.

Your job is to analyze the document with deep understanding of structure, meaning, and hierarchy.

====================================================
📌 CORE REQUIREMENTS
====================================================

1. Detect REAL headings and subheadings from the document.
2. Preserve original meaning and structure.
3. Do NOT split randomly or treat as chunks.
4. Do NOT invent section numbers.
5. Maintain logical flow.

====================================================
📌 OUTPUT FORMAT
====================================================

- Use **BOLD HEADINGS**
- Write structured paragraphs under each heading
- Maintain clean spacing

====================================================
📌 FINAL SECTION

### KEY INSIGHTS
- Bullet points only (important insights)

### KEYWORDS
- Bullet points only (important terms)

====================================================
DOCUMENT:
{text}

FINAL REPORT:
"""

    return prompt


# ==========================================
# SUMMARIZATION FUNCTION
# ==========================================

def summarize_text(text):

    prompt = create_summary_prompt(text)

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are a document intelligence system."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.3
    )

    return response.choices[0].message.content
