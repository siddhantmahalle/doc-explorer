from fastapi import FastAPI, UploadFile, File
from api.models.chat_request import ChatRequest
from api.process_document.document_processor import ProcessDocument
from api.query_document.query_chain import QueryDoc

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

file_loc = "uploads/llms.pdf"
file_type = "application/pdf"

processor = ProcessDocument()
doc_query = QueryDoc()

# Placeholder dictionary to store task references
task_dict = {}


@app.get("/api")
async def root():
    return {"message": "Doc Explorer API"}


@app.post("/api/upload")
async def upload(file: UploadFile = File(...)) -> dict:
    """
    Upload a file for analysis

    Args:
        file: file to be uploaded

    Returns:
        JSON: JSON object with the results of the analysis
    """
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        contents = await file.read()
        buffer.write(contents)

    global file_loc, file_type
    file_loc = file_path
    file_type = file.content_type

    return {"message": f"processing {file.filename}"}


@app.post("/api/process_status")
async def process_status() -> dict:
    global file_loc, file_type
    processor.process(document=file_loc, file_type=file_type)

    return {"status": "complete"}


@app.post("/api/chat")
async def chatbot(chat_request: ChatRequest) -> dict:
    """
    Chatbot API

    Args:
        chat_request: message to be processed

    Returns:
        JSON: JSON object with the response
    """
    # response = f"This is the default response for {chat_request.message}"
    search_index = processor.get_search_index()
    search_docs = search_index.similarity_search(query=chat_request.message)
    response = doc_query.query(query=chat_request.message, search_docs=search_docs)

    return {"response": response}
