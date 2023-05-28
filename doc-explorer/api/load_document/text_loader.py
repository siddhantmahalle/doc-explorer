import os
from fastapi import File
from langchain.document_loaders import TextLoader


async def load_text(file: File(...)):

    text_loader = TextLoader(file)
    document = text_loader.load()
    return document
