from fastapi import APIRouter, HTTPException

from models.translation_models import TranslationRequest, TranslationResponse
from services.translation_services import Translator

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
