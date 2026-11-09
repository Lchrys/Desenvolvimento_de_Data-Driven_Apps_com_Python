from fastapi import FastAPI
from routers.translation_routers import router

app = FastAPI(title="Tradução inglês-alemão com LangChain")
app.include_router(router)
