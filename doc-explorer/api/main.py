import asyncio
from fastapi import FastAPI, UploadFile, File
from api.models.chat_request import ChatRequest
from api.process_document import ProcessDocument
from api.query_document import QueryDoc

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


processor = ProcessDocument()
doc_query = QueryDoc()

# Placeholder dictionary to store task references
task_dict = {}


@app.get("/api/python")
def root():
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
    file_type = file.content_type
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        contents = await file.read()
        buffer.write(contents)

    task = asyncio.create_task(processor.process(document=file_path, file_type=file_type))
    global task_dict
    task_dict["processing_task"] = task
    return {"message": f"processing {file.filename}"}


@app.get("http://127.0.0.1:8000/api/process_status")
async def process_status():
    # Check the processing status
    global task_dict
    if "processing_task" in task_dict:
        task = task_dict["processing_task"]
        await task
        task_dict.pop("processing_task")

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
