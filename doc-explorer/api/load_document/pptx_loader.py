import os
from fastapi import File
from langchain.document_loaders import UnstructuredPowerPointLoader


def load_pptx(file: File(...)):

    ppt_loader = UnstructuredPowerPointLoader(file)
    document = ppt_loader.load()
    return document
