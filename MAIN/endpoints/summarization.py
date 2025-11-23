from fastapi import APIRouter
import regex as re
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
from MAIN.schemas.text_request import SummarizeRequest
from MAIN.schemas.text_response import SummarizeResponse

router = APIRouter()

MODEL = "t5-small"


def preprocess_text(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def generate_summary(text: str, max_length: int, min_length: int) -> str:
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL)
    tokenizer = AutoTokenizer.from_pretrained(MODEL)

    cleaned_text = preprocess_text(text)
    tokenized = tokenizer(cleaned_text, return_tensors="pt")

    with torch.no_grad():
        output = model.generate(
            **tokenized,
            max_length=max_length,
            min_length=min_length,
            num_beams=5,
            early_stopping=True,
        )
        summary = tokenizer.decode(output[0], skip_special_tokens=True)
        return summary


@router.post("/summarize", response_model=SummarizeResponse)
def summarize(payload: SummarizeRequest) -> SummarizeResponse:
    summary = generate_summary(payload.text, payload.max_length, payload.min_length)
    return SummarizeResponse(summary=summary)

