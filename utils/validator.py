
import os
import fitz  # PyMuPDF

from config import (
    MAX_FILE_SIZE_MB,
    MAX_PAGES,
    MAX_WORDS,
    SUPPORTED_EXTENSIONS
)

# ------------------------------------------
# Check file extension
# ------------------------------------------
def validate_file_extension(file_path):
    return os.path.splitext(file_path)[1].lower() in SUPPORTED_EXTENSIONS


# ------------------------------------------
# Check file size
# ------------------------------------------
def validate_file_size(file_path):
    size_mb = os.path.getsize(file_path) / (1024 * 1024)
    return size_mb <= MAX_FILE_SIZE_MB


# ------------------------------------------
# Check page count
# ------------------------------------------
def validate_page_count(file_path):
    doc = fitz.open(file_path)
    pages = len(doc)
    doc.close()
    return pages <= MAX_PAGES


# ------------------------------------------
# Extract text (for validation only)
# ------------------------------------------
def extract_text(file_path):
    doc = fitz.open(file_path)
    text = ""

    for page in doc:
        text += page.get_text()

    doc.close()
    return text


# ------------------------------------------
# Check word count
# ------------------------------------------
def validate_word_count(text):
    words = text.replace("\n", " ").split()
    return len(words) <= MAX_WORDS


# ------------------------------------------
# Detect scanned PDF (simple heuristic)
# ------------------------------------------
def validate_digital_pdf(text):
    words = text.replace("\n", " ").split()
    return len(words) > 50


# ------------------------------------------
# MASTER VALIDATOR
# ------------------------------------------
def validate_pdf(file_path):

    if not validate_file_extension(file_path):
        return False, "Only PDF files allowed"

    if not validate_file_size(file_path):
        return False, "File exceeds size limit"

    if not validate_page_count(file_path):
        return False, "File exceeds page limit"

    text = extract_text(file_path)

    if not validate_digital_pdf(text):
        return False, "Scanned PDFs not supported"

    if not validate_word_count(text):
        return False, "File exceeds word limit"

    return True, "PDF is valid"
