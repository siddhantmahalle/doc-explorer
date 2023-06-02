import os
from fastapi import File
from langchain.document_loaders import PyPDFLoader


def load_pdf(file: str):

    pdf_loader = PyPDFLoader(file)
    document = pdf_loader.load_and_split()
    return document
