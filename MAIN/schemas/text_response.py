from pydantic import BaseModel
from typing import List

class SummarizeResponse(BaseModel):
    summary: str


class KeywordResponse(BaseModel):
    keywords: List[str]


class SentimentResponse(BaseModel):
    sentiment: str
    confidence: float


class LanguageResponse(BaseModel):
    language: str
    probability: float


class CleanTextResponse(BaseModel):
    cleaned_text: str
