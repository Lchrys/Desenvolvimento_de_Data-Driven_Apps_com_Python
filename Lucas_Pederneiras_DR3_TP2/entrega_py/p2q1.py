"""Parte 2 - Questão 1: chatbot simples com Fake LLM (FastAPI + LangChain).

Executar: python -m uvicorn p2q1:app --reload
Exemplo:  POST /chat  {"message": "Em qual continente fica o Brasil?"}
"""
from fastapi import APIRouter, FastAPI
from langchain_community.llms import FakeListLLM
from pydantic import BaseModel, Field

# ---------- models ----------


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)


class ChatResponse(BaseModel):
    message: str
    response: str


# ---------- services ----------

RESPONSES = {
    "olá": "Olá! Como posso ajudar?",
    "qual é o seu nome?": "Sou um chatbot de teste com Fake LLM.",
    "em qual continente fica o brasil?": "América do Sul",
    "como você funciona?": "Eu simulo respostas prontas para testar o fluxo da aplicação.",
}


class Chatbot:
    def __init__(self, message):
        self.message = message
        self.response = ""

    def run(self):
        key = self.message.strip().lower()
        answer = RESPONSES.get(
            key,
            "Desculpe, não posso responder essa pergunta no momento.",
        )
        llm = FakeListLLM(responses=[answer])
        self.response = llm.invoke(self.message)
        return self.response


# ---------- routers ----------

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(chat_request: ChatRequest):
    chatbot = Chatbot(chat_request.message)
    chatbot.run()
    return ChatResponse(message=chatbot.message, response=chatbot.response)


# ---------- app ----------

app = FastAPI(title="Chatbot com Fake LLM")
app.include_router(router)
