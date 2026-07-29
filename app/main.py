"""
Main entry point for PatchContext.
"""

from fastapi import FastAPI

app = FastAPI(
    title="PatchContext",
    description="RAG over FastAPI development history",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to PatchContext!"
    }
