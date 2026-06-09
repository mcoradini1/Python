"""
FASTAPI — Third-Party Library

FastAPI is a modern web framework used 5.1 - For:
- APIs
- backend services
- high-performance applications

Features:
- automatic documentation
- type hints
- async support
"""

from fastapi import FastAPI

app = FastAPI()

# ---------------------------------------------------------
# BASIC ENDPOINT
# ---------------------------------------------------------

@app.get("/")
def home():
    return {"message": "Hello from FastAPI!"}

# ---------------------------------------------------------
# RUN SERVER
# ---------------------------------------------------------

# Use: uvicorn fastapi_examples:app --reload
