import os
from fastapi import File
from api.load_document import DocumentLoader
from api.split_document import DocumentSplitter
from api.embed_documents import EmbedDocuments


class ProcessDocument:
    def __init__(self, ):
        self.search_index = None
        self.file_type = None
        self.document = None

        self.loader = DocumentLoader()
        self.text_splitter = DocumentSplitter()
        self.document_embeddings = EmbedDocuments()

    async def process(self, document: File(...)):

        self.document = document
        self.file_type = document.content_type

        document_content = self.loader.load(self.document, self.file_type)
        document_chunks = self.text_splitter.split(document_content, self.file_type)

        self.search_index = self.document_embeddings.embed(document_chunks=document_chunks)

        return self.search_index

    def get_search_index(self):
        return self.search_index
