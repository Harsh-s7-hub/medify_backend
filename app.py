from fastapi import FastAPI
from pydantic import BaseModel

from rag_engine import retrieve_context
from inference import generate_answer

app = FastAPI(
    title="Medify AI Backend",
    version="1.0"
)

class ChatRequest(BaseModel):
    question: str

@app.get("/")
async def root():

    return {
        "message": "Medify AI Backend Running"
    }

@app.get("/health")
async def health():

    return {
        "status": "healthy"
    }

@app.post("/chat")
async def chat(req: ChatRequest):

    question = req.question.strip()

    context = retrieve_context(question)

    prompt = f"""
    Medical Context:
    {context}

    User Question:
    {question}

    Answer medically and clearly.
    """

    response = generate_answer(prompt)

    return {
        "question": question,
        "context": context,
        "response": response
    }