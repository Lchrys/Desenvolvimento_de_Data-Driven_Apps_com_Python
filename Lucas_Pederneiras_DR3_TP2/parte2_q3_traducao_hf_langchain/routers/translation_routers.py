from fastapi import APIRouter

from models.translation_models import TranslationRequest, TranslationResponse
from services.translation_services import Translator

router = APIRouter()


@router.post("/translate", response_model=TranslationResponse)
async def translate(translation_request: TranslationRequest):
    translator = Translator(translation_request.text)
    translator.run()
    return TranslationResponse(
        original_text=translator.text,
        translated_text=translator.response,
    )
