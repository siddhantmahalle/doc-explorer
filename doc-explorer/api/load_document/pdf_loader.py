import os
from fastapi import File
from langchain.document_loaders import PyPDFLoader


async def load_pdf(file: File(...)):

    pdf_loader = PyPDFLoader(file)
    document = pdf_loader.load()
    return document
