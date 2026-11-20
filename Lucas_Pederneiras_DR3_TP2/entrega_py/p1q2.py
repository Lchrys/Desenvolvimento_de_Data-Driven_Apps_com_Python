"""Parte 1 - Questão 2: tradução inglês -> francês (FastAPI + Helsinki-NLP/opus-mt-en-fr).

Executar: python -m uvicorn p1q2:app --reload
Exemplo:  POST /translate  {"text": "Hello, how are you?"}
"""
import re

from fastapi import APIRouter, FastAPI
from pydantic import BaseModel, Field
from transformers import pipeline

# ---------- models ----------


class TranslationRequest(BaseModel):
    text: str = Field(min_length=1)


class TranslationResponse(BaseModel):
    original_text: str
    translated_text: str


# ---------- services ----------

pipe = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")


class Translator:
    def __init__(self, text):
        self.text = text
        self.response = ""

    def run(self):
        sentences = [
            s.strip()
            for s in re.split(r"(?<=[.!?])\s+", self.text.strip())
            if s.strip()
        ]
        if len(sentences) <= 1:
            result = pipe(self.text)
            self.response = result[0]["translation_text"]
        else:
            results = pipe(sentences)
            translated = [item["translation_text"] for item in results]
            self.response = " ".join(translated)
        return self.response


# ---------- routers ----------

router = APIRouter()


@router.post("/translate", response_model=TranslationResponse)
async def translate(translation_request: TranslationRequest):
    translator = Translator(translation_request.text)
    translator.run()
    return TranslationResponse(
        original_text=translator.text,
        translated_text=translator.response,
    )


# ---------- app ----------

app = FastAPI(title="Tradução inglês-francês")
app.include_router(router)
