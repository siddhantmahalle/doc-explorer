import os
import logging
from fastapi import File
from api.load_document import DocumentLoader
from api.split_document import DocumentSplitter
from api.embed_documents import EmbedDocuments

logging.basicConfig(level=logging.INFO)


class ProcessDocument:
    def __init__(self, ):
        self.search_index = None
        self.file_type = None
        self.document = None

        self.loader = DocumentLoader()
        self.text_splitter = DocumentSplitter()
        self.document_embeddings = EmbedDocuments()

    def process(self, document: str, file_type: str):

        self.document = document
        self.file_type = file_type

        logging.info("Loading Document")
        document_content = self.loader.load(self.document, self.file_type)
        logging.info("Loading done,Splitting Document")
        document_chunks = self.text_splitter.split(document_content, self.file_type)
        logging.info("Splitting done, Embedding Document")
        self.search_index = self.document_embeddings.embed(document_chunks=document_chunks)
        logging.info("Embedding done, returning search index")
        return self.search_index

    def get_search_index(self):
        return self.search_index
