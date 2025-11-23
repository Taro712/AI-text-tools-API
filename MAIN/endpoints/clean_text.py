import regex as re
from fastapi import APIRouter
from MAIN.schemas.text_request import CleanTextRequest
from MAIN.schemas.text_response import CleanTextResponse

router = APIRouter()


def clean_text(
    text: str,
    *,
    lowercase: bool,
    remove_punctuation: bool,
    remove_stopwords: bool,
) -> str:
    cleaned = text
    if lowercase:
        cleaned = cleaned.lower()
    if remove_punctuation:
        cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    cleaned = cleaned.strip()
    if remove_stopwords:
        cleaned = " ".join(
            token
            for token in cleaned.split()
            if token.lower() not in {"a", "an", "the", "and", "or", "but"}
        )
    return cleaned


@router.post("/clean", response_model=CleanTextResponse)
def cleaned_text(payload: CleanTextRequest) -> CleanTextResponse:
    cleaned = clean_text(
        payload.text,
        lowercase=payload.lowercase,
        remove_punctuation=payload.remove_punctuation,
        remove_stopwords=payload.remove_stopwords,
    )
    return CleanTextResponse(cleaned_text=cleaned)

