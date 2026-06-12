from fastapi import FastAPI
from pydantic import BaseModel

from rag import ask_rag

app = FastAPI()


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "VulnStore AI"
    }


@app.post("/chat")
def chat(req: ChatRequest):

    answer = ask_rag(
        req.question
    )

    return {
        "answer": answer
    }