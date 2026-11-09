from fastapi import FastAPI
from routers.translation_routers import router

app = FastAPI(title="Tradução inglês-francês com OpenAI")
app.include_router(router)
