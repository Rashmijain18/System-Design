from fastapi import FastAPI
import os

app = FastAPI()

SERVER_NAME = os.getenv("SERVER_NAME", "UNKNOWN")

@app.get("/")
def read_root():
    return {"message": f"Response from {SERVER_NAME}"}

@app.get("/health")
def health():
    return {"status": "ok"}