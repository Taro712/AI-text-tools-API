from pydantic import BaseModel

class SummarizeRequest(BaseModel):
    text: str
    max_length: int = 120
    min_length: int = 30


class KeywordRequest(BaseModel):
    text: str
    top_n: int = 5


class SentimentRequest(BaseModel):
    text: str


class LanguageRequest(BaseModel):
    text: str


class CleanTextRequest(BaseModel):
    text: str
    lowercase: bool = True
    remove_punctuation: bool = True
    remove_stopwords: bool = True
