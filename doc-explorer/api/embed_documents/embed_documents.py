import os
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings

pinecone.init(
    api_key=os.environ['PINECONE_API_KEY'],
    environment=os.environ['PINECONE_ENVIRONMENT']
)


class EmbedDocuments:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()

    def embed(self, document_chunks):

        search_index = Pinecone.from_documents(documents=[document_chunks], embedding=self.embeddings)
        return search_index
