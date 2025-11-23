from typing import List
import regex as re
import yake
from fastapi import APIRouter
from MAIN.schemas.text_request import KeywordRequest
from MAIN.schemas.text_response import KeywordResponse

router = APIRouter()


def process(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def keyword_extract(text: str, top_n: int) -> List[str]:
    cleaned_text = process(text)
    extractor = yake.KeywordExtractor(
        top_k=max(top_n, 1),
        top_percent=0.5,
        deduplication_threshold=0.9,
        deduplication_algo="seqm",
        window_size=1,
        use_mmr=True,
        diversity_ratio=0.5,
        n_gram_range=(1, 3),
        lan="en",
    )
    keywords = extractor.extract_keywords(cleaned_text)
    return [keyword for keyword, _score in keywords]


@router.post("/keywords", response_model=KeywordResponse)
def extract_keywords(payload: KeywordRequest) -> KeywordResponse:
    keywords = keyword_extract(payload.text, payload.top_n)
    return KeywordResponse(keywords=keywords)