from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)


def split_text(text):
    document_chunks = splitter.split_documents(text)
    return document_chunks
