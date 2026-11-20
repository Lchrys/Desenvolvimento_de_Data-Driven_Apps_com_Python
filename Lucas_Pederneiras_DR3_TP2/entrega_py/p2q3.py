"""Parte 2 - Questão 3: tradução inglês -> alemão (LangChain + Helsinki-NLP/opus-mt-en-de).

Executar: python -m uvicorn p2q3:app --reload
Exemplo:  POST /translate  {"text": "Hello, how are you?"}
"""
from fastapi import APIRouter, FastAPI
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from pydantic import BaseModel, Field
from transformers import pipeline

# ---------- models ----------


class TranslationRequest(BaseModel):
    text: str = Field(min_length=1)


class TranslationResponse(BaseModel):
    original_text: str
    translated_text: str


# ---------- services ----------

pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
llm = HuggingFacePipeline(pipeline=pipe)
prompt = PromptTemplate.from_template("{text}")
chain = prompt | llm


class Translator:
    def __init__(self, text):
        self.text = text
        self.response = ""

    def run(self):
        self.response = chain.invoke({"text": self.text})
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

app = FastAPI(title="Tradução inglês-alemão com LangChain")
app.include_router(router)
