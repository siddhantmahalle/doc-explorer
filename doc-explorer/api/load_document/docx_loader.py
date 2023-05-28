import os
from fastapi import File
from langchain.document_loaders import UnstructuredWordDocumentLoader


async def load_docx(file: File(...)):

    docx_loader = UnstructuredWordDocumentLoader(file)
    document = docx_loader.load()
    return document
