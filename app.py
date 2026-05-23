from fastapi import FastAPI
from pydantic import BaseModel

from rag_engine import retrieve_context
from inference import generate_answer

app = FastAPI()

class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
async def chat(req: ChatRequest):

    question = req.question

    context = retrieve_context(question)

    prompt = f"""
    You are a helpful medical AI assistant.

    Context:
    {context}

    Question:
    {question}

    Give a medically relevant answer.
    """

    response = generate_answer(prompt)

    return {
        "question": question,
        "response": response
    }