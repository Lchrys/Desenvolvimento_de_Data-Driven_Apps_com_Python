from fastapi import APIRouter

from models.generation_models import GenerationRequest, GenerationResponse
from services.generation_services import TextGenerator

router = APIRouter()


@router.post("/generate", response_model=GenerationResponse)
async def generate(generation_request: GenerationRequest):
    generator = TextGenerator(generation_request.text)
    generator.run()
    return GenerationResponse(input=generator.text, generated_text=generator.response)
