# ============================================================
#                    🌐 FASTAPI SERVER
# ============================================================

from fastapi import FastAPI
from pydantic import BaseModel

from agent import chat_with_agent


# Create the FastAPI application
app = FastAPI(
    title="City Intelligence Agent",
    description="API for interacting with the City Intelligence Agent",
    version="1.0.0"
)


# ============================================================
#                 📨 REQUEST MODEL
# ============================================================

class ChatRequest(BaseModel):
    """
    Model for the user's chat request.
    """

    message: str


@app.get("/")
def home():
    """
    Home endpoint.
    """

    return {
        "message": "Welcome to the City Intelligence Agent API!"
    }


# ============================================================
#                 🤖 CHAT ENDPOINT
# ============================================================

@app.post("/chat")
def chat(request: ChatRequest):
    """
    Send a message to the AI agent and return its response.
    """

    response = chat_with_agent(request.message)

    return {
        "response": response
    }