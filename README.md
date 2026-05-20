# 📄 SmartPDF Insight Engine

<p align="center">
  <img src="assets/banner.png" width="100%">
</p>

<h3 align="center">
AI-Powered Document Intelligence System with Semantic Retrieval, FAISS Vector Search, Hierarchical Summarization, and RAG-based Question Answering
</h3>

---

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge&logo=streamlit)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-green?style=for-the-badge)
![LLM](https://img.shields.io/badge/LLM-Groq-orange?style=for-the-badge)
![RAG](https://img.shields.io/badge/RAG-Enabled-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

<p align="center">
  <a href="https://smartpdf-insight-engine.onrender.com">
    <img src="https://img.shields.io/badge/🚀_Live_Demo-Open_App-success?style=for-the-badge">
  </a>

  <a href="https://github.com/sivakavihemalatha-hub/smartpdf-insight-engine">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github">
  </a>
</p>

---

# 📑 Table of Contents

- [Overview](#-overview)
- [How It Works](#-how-it-works)
- [Problem Statement](#-problem-statement)
- [Key Features](#-key-features)
- [System Architecture](#️-system-architecture)
- [AI Pipeline Explanation](#-ai-pipeline-explanation)
- [Tech Stack](#️-tech-stack)
- [Project Structure](#-project-structure)
- [Application Screenshots](#-application-screenshots)
- [Installation](#️-installation)
- [Live Demo & Deployment](#-live-demo--deployment)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [License](#-license)

---

# 🚀 Overview

SmartPDF Insight Engine is an advanced AI-powered document intelligence system designed to intelligently process, summarize, retrieve, and answer questions from PDF documents using modern Natural Language Processing (NLP) and Retrieval-Augmented Generation (RAG) techniques.

The system combines semantic retrieval, vector search, hierarchical summarization, and context-aware question answering to transform traditional PDF documents into intelligent interactive knowledge systems.

---

# 🔄 How It Works

1. Upload a PDF document  
2. Extract and clean document content  
3. Perform semantic chunking  
4. Generate vector embeddings  
5. Store embeddings using FAISS  
6. Generate AI-powered summaries and insights  
7. Ask context-aware questions using RAG  

---

# 🎯 Problem Statement

Traditional PDF readers struggle to provide intelligent understanding of large and complex documents.

Users often face:
- Time-consuming manual reading
- Difficulty extracting key insights
- Poor semantic search capabilities
- Lack of contextual question answering
- Inefficient navigation through lengthy documents

SmartPDF Insight Engine solves these challenges using AI-powered document intelligence pipelines and semantic retrieval systems.

---

# ✨ Key Features

## 📄 Intelligent PDF Processing
- PDF validation and verification
- Page limit and file size handling
- Detection of unsupported or scanned PDFs

## 🧹 Advanced Text Cleaning
- Removes noisy formatting
- Cleans invisible characters
- Preserves semantic readability
- Normalizes document structure

## ✂️ Semantic Chunking
- Recursive semantic text splitting
- Context-preserving overlap strategy
- Retrieval-optimized chunk generation

## 🧠 Embedding Generation
- SentenceTransformer-based embeddings
- Semantic vector representation
- Efficient embedding pipeline

## 🔍 FAISS Vector Retrieval
- High-speed semantic similarity search
- Efficient nearest-neighbor retrieval
- Vector indexing for scalable search

## 📌 Hierarchical AI Summarization
- Heading-aware summarization
- Key insight extraction
- Intelligent keyword generation
- Structured summary generation

## 💬 RAG-based Question Answering
- Context-aware answer generation
- Retrieval-grounded responses
- Reduced hallucinations using semantic retrieval

## 🌐 Interactive Streamlit Interface
- Real-time PDF upload interface
- AI-generated summaries and insights
- Conversational document chat system

---

# 🏗️ System Architecture

## Complete Pipeline Workflow

<p align="center">
  <img src="assets/architecture.png" width="100%">
</p>

---

# 🧠 AI Pipeline Explanation

## 1️⃣ PDF Validation

The uploaded PDF document is validated using:
- File extension checking
- File size constraints
- Page count validation
- Word limit validation
- Digital PDF verification

---

## 2️⃣ Content Extraction

The system extracts:
- Page-wise text using PyMuPDF
- Structured tables using pdfplumber

The extracted content is merged into a unified document structure for downstream processing.

---

## 3️⃣ Text Cleaning

The preprocessing pipeline:
- Removes unnecessary spaces
- Cleans invisible characters
- Normalizes formatting
- Preserves semantic readability

---

## 4️⃣ Semantic Chunking

The cleaned text is divided using:

`RecursiveCharacterTextSplitter`

### Features
- Context-preserving overlap
- Semantic chunk segmentation
- Retrieval-optimized structure

---

## 5️⃣ Embedding Generation

Document chunks are converted into semantic vectors using:

`sentence-transformers/paraphrase-MiniLM-L3-v2`

This enables semantic similarity search and efficient retrieval.

---

## 6️⃣ FAISS Vector Search

The generated embeddings are stored in a FAISS vector database for:
- High-speed retrieval
- Semantic search
- Efficient nearest-neighbor lookup

---

## 7️⃣ Hierarchical Summarization

The summarization engine:
- Detects headings and subheadings
- Preserves document hierarchy
- Extracts important insights
- Generates structured summaries

### Powered By
- Groq LLM API
- Llama-3.3-70B-Versatile

---

## 8️⃣ Retrieval-Augmented Generation (RAG)

When a user asks a question:
1. Relevant chunks are retrieved
2. Context is constructed
3. The LLM generates grounded answers
4. Hallucinations are minimized through retrieval grounding

---

# 🛠️ Tech Stack

| Category | Technologies Used |
|---|---|
| Frontend | Streamlit |
| Programming Language | Python |
| PDF Processing | PyMuPDF, pdfplumber |
| NLP | NLTK |
| Semantic Chunking | LangChain Text Splitters |
| Embeddings | SentenceTransformers |
| Embedding Model | paraphrase-MiniLM-L3-v2 |
| Vector Database | FAISS |
| LLM Provider | Groq |
| LLM Model | Llama-3.3-70B-Versatile |
| Machine Learning | Scikit-learn |
| Deployment | Render |

---

# 📂 Project Structure

```bash
smartpdf-insight-engine/
│
├── app.py
├── main.py
├── config.py
├── requirements.txt
├── LICENSE
├── README.md
├── .gitignore
│
├── assets/
│   ├── banner.png
│   ├── architecture.png
│   └── screenshots/
│       ├── interface.png
│       ├── pdf_uploaded.png
│       ├── summary.png
│       ├── insights_keywords.png
│       └── qa_output.png
│
└── utils/
    ├── validator.py
    ├── pdf_extractor.py
    ├── cleaner.py
    ├── chunker.py
    ├── embedding_generator.py
    ├── faiss_manager.py
    ├── summarizer.py
    ├── retriever.py
    └── rag_engine.py
```

---

# 📸 Application Screenshots

---

## 1️⃣ Interface (Before Upload)

<p align="center">
  <img src="assets/screenshots/interface.png" width="90%">
</p>

---

## 2️⃣ PDF Uploaded

<p align="center">
  <img src="assets/screenshots/pdf_uploaded.png" width="90%">
</p>

---

## 3️⃣ AI Summary Output

<p align="center">
  <img src="assets/screenshots/summary.png" width="90%">
</p>

---

## 4️⃣ Keywords & Insights

<p align="center">
  <img src="assets/screenshots/insights_keywords.png" width="90%">
</p>

---

## 5️⃣ Chat / RAG Question Answering

<p align="center">
  <img src="assets/screenshots/qa_output.png" width="90%">
</p>

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/sivakavihemalatha-hub/smartpdf-insight-engine.git
```

---

## Move into Project Directory

```bash
cd smartpdf-insight-engine
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 🚀 Live Demo & Deployment

## Deployment Platforms
- Render
- Streamlit Framework

## Live Application

[Open SmartPDF Insight Engine](https://smartpdf-insight-engine.onrender.com)

---

# 📈 Future Improvements

- Multi-document analysis
- OCR support for scanned handwritten PDFs
- Hybrid retrieval pipelines
- Knowledge graph integration
- Citation-aware responses
- Agentic AI workflows
- Multi-language document understanding
- Cloud vector database integration

---

# 👩‍💻 Author

## Hemalatha Sivakavi

AI/ML Enthusiast • Generative AI Developer • Document Intelligence Systems

🔗 GitHub:
https://github.com/sivakavihemalatha-hub

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
