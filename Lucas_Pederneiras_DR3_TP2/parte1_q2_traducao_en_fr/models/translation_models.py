from pydantic import BaseModel, Field


class TranslationRequest(BaseModel):
    text: str = Field(min_length=1)


class TranslationResponse(BaseModel):
    original_text: str
    translated_text: str
