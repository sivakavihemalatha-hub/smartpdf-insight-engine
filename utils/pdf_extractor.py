
# ==========================================
# IMPORTS
# ==========================================

import fitz  # PyMuPDF
import pdfplumber


# ==========================================
# FUNCTION:
# extract_text_pymupdf()
#
# PURPOSE:
# Extract normal text from PDF
# page by page
# ==========================================
def extract_text_pymupdf(file_path):

    document = fitz.open(file_path)

    extracted_pages = []

    for page_number, page in enumerate(document):

        text = page.get_text()

        extracted_pages.append({
            "page_number": page_number + 1,
            "text": text
        })

    document.close()

    return extracted_pages


# ==========================================
# FUNCTION:
# extract_tables_pdfplumber()
#
# PURPOSE:
# Extract simple tables from PDF
# ==========================================
def extract_tables_pdfplumber(file_path):

    extracted_tables = []

    with pdfplumber.open(file_path) as pdf:

        for page_number, page in enumerate(pdf.pages):

            tables = page.extract_tables()

            for table in tables:

                extracted_tables.append({
                    "page_number": page_number + 1,
                    "table": table
                })

    return extracted_tables


# ==========================================
# FUNCTION:
# combine_extracted_content()
#
# PURPOSE:
# Combine extracted text + tables
# into one clean structure
# ==========================================
def combine_extracted_content(text_pages, tables):

    combined_content = ""

    # Add page-wise text
    for page_data in text_pages:

        combined_content += f"\n\n--- Page {page_data['page_number']} ---\n"

        combined_content += page_data["text"]

    # Add extracted tables
    if tables:

        combined_content += "\n\n=== Extracted Tables ===\n"

        for table_data in tables:

            combined_content += f"\nPage {table_data['page_number']} Table:\n"

            table = table_data["table"]

            for row in table:

                combined_content += " | ".join(
                    [str(cell) if cell else "" for cell in row]
                )

                combined_content += "\n"

    return combined_content


# ==========================================
# FUNCTION:
# extract_pdf_content()
#
# PURPOSE:
# Main extraction pipeline
# ==========================================
def extract_pdf_content(file_path):

    # Extract normal text
    text_pages = extract_text_pymupdf(file_path)

    # Extract simple tables
    tables = extract_tables_pdfplumber(file_path)

    # Combine everything
    combined_content = combine_extracted_content(
        text_pages,
        tables
    )

    return combined_content
