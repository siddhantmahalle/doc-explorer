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
        self.pinecone_index_name = os.environ['PINECONE_INDEX_NAME']

    def embed(self, document_chunks):

        search_index = Pinecone.from_documents(documents=document_chunks,
                                               embedding=self.embeddings,
                                               index_name=self.pinecone_index_name)
        return search_index
