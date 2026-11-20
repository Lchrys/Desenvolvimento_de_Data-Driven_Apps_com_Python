"""Parte 2 - Questão 2: tradução inglês -> francês com OpenAI via LangChain.

Requer a variável OPENAI_API_KEY (arquivo .env ou ambiente).
Executar: python -m uvicorn p2q2:app --reload
Exemplo:  POST /translate  {"text": "Hello, how are you?"}
"""
import os

from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI, HTTPException
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

# ---------- models ----------


class TranslationRequest(BaseModel):
    text: str = Field(min_length=1)


class TranslationResponse(BaseModel):
    original_text: str
    translated_text: str


# ---------- services ----------

load_dotenv()

prompt = PromptTemplate.from_template(
    "Translate the following English text to French: {text}"
)
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY"),
)
chain = prompt | llm | StrOutputParser()


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
    try:
        translator.run()
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="Erro ao chamar a API da OpenAI.",
        )
    return TranslationResponse(
        original_text=translator.text,
        translated_text=translator.response,
    )


# ---------- app ----------

app = FastAPI(title="Tradução inglês-francês com OpenAI")
app.include_router(router)
