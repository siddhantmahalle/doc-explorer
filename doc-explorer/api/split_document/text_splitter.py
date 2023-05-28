from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunkSize=100, chunkOverlap=20)


def split_text(text):
    document_chunks = splitter.split_documents(text)
    return document_chunks
