
import streamlit as st
import os
import sys

# ==========================================
# CONNECT BACKEND
# ==========================================

sys.path.append(".")

from main import process_document, ask_document_question

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Smart PDF AI",
    layout="wide"
)

st.title("📄 Smart PDF Intelligence System")

# ==========================================
# SESSION STATE
# ==========================================

if "document_id" not in st.session_state:
    st.session_state.document_id = None

if "summary" not in st.session_state:
    st.session_state.summary = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ==========================================
# UPLOAD PDF SECTION
# ==========================================

st.header("📤 Upload PDF")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

# ==========================================
# PROCESS DOCUMENT
# ==========================================

if uploaded_file is not None:

    UPLOAD_FOLDER = "uploads"

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.name
    )
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ PDF Uploaded Successfully!")

    if st.button("Process Document"):

        with st.spinner("Processing PDF..."):

            result = process_document(file_path)

        if result["status"] == "success":

            st.session_state.document_id = result["document_id"]

            st.session_state.summary = result["summary"]

            st.success("✅ Document Processed Successfully!")

        else:

            st.error(result["message"])

# ==========================================
# SHOW SUMMARY
# ==========================================

if st.session_state.summary:

    st.header("📌 Document Summary")

    st.write(st.session_state.summary)

# ==========================================
# CHAT WITH DOCUMENT
# ==========================================

if st.session_state.document_id:

    st.header("💬 Chat With Your Document")

    st.info(
        "This assistant answers only document-related questions "
        "based on the uploaded PDF."
    )

    # ======================================
    # DISPLAY CHAT HISTORY
    # ======================================

    for chat in st.session_state.chat_history:

        st.markdown(
            f"### 🧑 Question:  \n{chat['question']}"
        )

        st.markdown(
            f"### 🤖 Answer:  \n{chat['answer']}"
        )

        st.divider()

    # ======================================
    # QUESTION INPUT
    # ======================================

    question = st.text_input(
        "Enter your next question:",
        key=f"question_{len(st.session_state.chat_history)}"
    )

    # ======================================
    # ASK QUESTION BUTTON
    # ======================================

    if st.button(
        "Ask Question",
        key=f"button_{len(st.session_state.chat_history)}"
    ):

        if question.strip() != "":

            with st.spinner("Generating Answer..."):

                answer = ask_document_question(
                    question,
                    st.session_state.document_id
                )

            # ==============================
            # SAVE CHAT
            # ==============================

            st.session_state.chat_history.append({

                "question": question,
                "answer": answer

            })

            st.rerun()

        else:

            st.warning("⚠ Please enter a question.")
