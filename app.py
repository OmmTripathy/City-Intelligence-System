# ============================================================
#                    🌐 FASTAPI SERVER
# ============================================================

from fastapi import FastAPI

# Create the FastAPI application
app = FastAPI(
    title="City Intelligence Agent",
    description="API for interacting with the City Intelligence Agent",
    version="1.0.0"
)


@app.get("/")
def home():
    """
    Home endpoint.

    Visit:
    http://127.0.0.1:8000
    """

    return {
        "message": "Welcome to the City Intelligence Agent API!"
    }