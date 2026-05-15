
# ==========================================
# IMPORTS
# ==========================================

import re


# ==========================================
# FUNCTION:
# remove_extra_spaces()
#
# PURPOSE:
# Replace multiple spaces with single space
# ==========================================
def remove_extra_spaces(text):

    text = re.sub(r"[ ]+", " ", text)

    return text


# ==========================================
# FUNCTION:
# normalize_newlines()
#
# PURPOSE:
# Preserve paragraph structure
# while removing excessive empty lines
# ==========================================
def normalize_newlines(text):

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text


# ==========================================
# FUNCTION:
# clean_special_characters()
#
# PURPOSE:
# Remove unwanted invisible characters
# ==========================================
def clean_special_characters(text):

    text = text.replace("\x00", "")

    return text


# ==========================================
# FUNCTION:
# clean_text()
#
# PURPOSE:
# Main text cleaning pipeline
# ==========================================
def clean_text(text):

    # Remove unwanted special characters
    text = clean_special_characters(text)

    # Normalize extra spaces
    text = remove_extra_spaces(text)

    # Normalize excessive newlines
    text = normalize_newlines(text)

    # Remove leading/trailing spaces
    text = text.strip()

    return text
