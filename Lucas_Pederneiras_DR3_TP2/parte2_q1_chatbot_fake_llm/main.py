from fastapi import FastAPI
from routers.chat_routers import router

app = FastAPI(title="Chatbot com Fake LLM")
app.include_router(router)
