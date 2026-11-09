from pydantic import BaseModel, Field


class GenerationRequest(BaseModel):
    text: str = Field(min_length=1)


class GenerationResponse(BaseModel):
    input: str
    generated_text: str
