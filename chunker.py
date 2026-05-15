
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP


def create_text_splitter():
    splitter = RecursiveCharacterTextSplitter(

        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,

        separators=[
            "\n\n",
            "\n",
            ". ",
            " "
        ]
    )

    return splitter


def chunk_text(cleaned_text):
    splitter = create_text_splitter()
    return splitter.split_text(cleaned_text)
