from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import process_query


app = FastAPI()

class Query(BaseModel):
    question:str

@app.post("/ask")
def ask(query:Query):
    answer = process_query(query.question)
    return {"answer":answer}
