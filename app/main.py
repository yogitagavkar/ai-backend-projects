from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.chatbot import handle_chat
from app.models import ChatRequest, ChatResponse, BillResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For demo. Restrict later.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Restaurant Chatbot API is running 🚀"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = handle_chat(request.user_input)

    if isinstance(result, dict) and "total" in result:
        return ChatResponse(bill=BillResponse(**result))

    return ChatResponse(response=str(result))