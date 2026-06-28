# ============================================================
#                    🌐 FASTAPI SERVER
# ============================================================

from fastapi import FastAPI
from pydantic import BaseModel

from agent import chat_with_agent
from fastapi.middleware.cors import CORSMiddleware

# Create the FastAPI application
app = FastAPI(
    title="City Intelligence Agent",
    description="API for interacting with the City Intelligence Agent",
    version="1.0.0"
)

# ============================================================
#                    CORS CONFIGURATION
# ============================================================

app.add_middleware(
    CORSMiddleware,

    # Allow requests from any frontend (development only)
    allow_origins=["*"],

    # Allow cookies if needed
    allow_credentials=True,

    # Allow all HTTP methods (GET, POST, etc.)
    allow_methods=["*"],

    # Allow all headers
    allow_headers=["*"],
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