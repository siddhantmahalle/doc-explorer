import asyncio
from fastapi import FastAPI, UploadFile, File
from api.models.chat_request import ChatRequest
from api.process_document import ProcessDocument
from api.query_document import QueryDoc

app = FastAPI()

processor = ProcessDocument()
doc_query = QueryDoc()

processing_status = "processing"

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


    global processing_status
    processing_status = "processing"
    task = asyncio.create_task(processor.process(document=file_path, file_type=file_type))
    task_dict["processing_task"] = task
    return {"message": f"processing {file.filename}"}


@app.get("/api/process-status")
async def process_status():
    # Check the processing status
    global processing_status
    if "processing_task" in task_dict:
        task = task_dict["processing_task"]
        await task

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
    search_docs = search_index.similarity_search(query=chat_request.message, include_meta=True)
    response = doc_query.query(query=chat_request.message, search_docs=search_docs)

    return {"response": response}
