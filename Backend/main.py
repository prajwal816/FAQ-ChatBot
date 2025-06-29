from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from chatbot import ask_question
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # <== VERY IMPORTANT!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class Query(BaseModel):
    query: str

# Endpoint to handle chat
@app.post("/ask")
def handle_question(query: Query):
    answer = ask_question(query.query)
    return {"answer": answer}

@app.get("/")
def root():
    return {"message": "FAQ Chatbot backend is running"}

