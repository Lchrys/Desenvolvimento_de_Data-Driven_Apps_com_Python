"""Parte 1 - Questão 1: geração de texto com GPT-2 (FastAPI + transformers).

Executar: python -m uvicorn p1q1:app --reload
Exemplo:  POST /generate  {"text": "Once upon a time"}
"""
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel, Field
from transformers import pipeline

# ---------- models ----------


class GenerationRequest(BaseModel):
    text: str = Field(min_length=1)


class GenerationResponse(BaseModel):
    input: str
    generated_text: str


# ---------- services ----------

pipe = pipeline("text-generation", model="gpt2")


class TextGenerator:
    def __init__(self, text):
        self.text = text
        self.response = ""

    def run(self):
        result = pipe(
            self.text,
            max_new_tokens=50,
            return_full_text=False,
            pad_token_id=pipe.tokenizer.eos_token_id,
        )
        self.response = result[0]["generated_text"]
        return self.response


# ---------- routers ----------

router = APIRouter()


@router.post("/generate", response_model=GenerationResponse)
async def generate(generation_request: GenerationRequest):
    generator = TextGenerator(generation_request.text)
    generator.run()
    return GenerationResponse(input=generator.text, generated_text=generator.response)


# ---------- app ----------

app = FastAPI(title="Geração de texto com GPT-2")
app.include_router(router)
