from fastapi import APIRouter

from models.chat_models import ChatRequest, ChatResponse
from services.chat_services import Chatbot

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(chat_request: ChatRequest):
    chatbot = Chatbot(chat_request.message)
    chatbot.run()
    return ChatResponse(message=chatbot.message, response=chatbot.response)
