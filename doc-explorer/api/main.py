from fastapi import FastAPI, UploadFile, File
from api.models.chat_request import ChatRequest
app = FastAPI()


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

    contents = await file.read()

    print("Received file:", file.filename)

    return {"message": f"File {file.filename} uploaded successfully"}


@app.post("/api/chat")
async def chatbot(chat_request: ChatRequest) -> dict:
    """
    Chatbot API

    Args:
        chat_request: message to be processed

    Returns:
        JSON: JSON object with the response
    """
    response = f"This is the default response for {chat_request.message}"

    return {"response": response}

