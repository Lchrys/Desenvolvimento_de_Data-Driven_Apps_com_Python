from fastapi import FastAPI
from routers.generation_routers import router

app = FastAPI(title="Geração de texto com GPT-2")
app.include_router(router)
