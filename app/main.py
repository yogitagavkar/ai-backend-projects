from fastapi import FastAPI
from app.chatbot import handle_chat
from app.models import ChatRequest, ChatResponse, BillResponse

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = handle_chat(request.user_input)

    if isinstance(result, dict) and "total" in result:
        return ChatResponse(bill=BillResponse(**result))

    return ChatResponse(response=str(result))   # ✅ ALWAYS STRING