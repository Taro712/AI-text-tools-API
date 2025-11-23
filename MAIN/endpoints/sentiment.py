from fastapi import APIRouter
import regex as re
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from MAIN.schemas.text_request import SentimentRequest
from MAIN.schemas.text_response import SentimentResponse

router = APIRouter()

MODEL = "distilbert-base-uncased-finetuned-sst-2-english"
LABELS = ("NEGATIVE", "POSITIVE")


def preprocess_text(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def predict_sentiment(text: str) -> SentimentResponse:
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    tokenizer = AutoTokenizer.from_pretrained(MODEL)

    cleaned_text = preprocess_text(text)
    tokenized = tokenizer(cleaned_text, return_tensors="pt")

    with torch.no_grad():
        output = model(**tokenized)
        logits = output.logits
        probabilities = torch.softmax(logits, dim=-1)
        confidence, prediction_idx = torch.max(probabilities, dim=-1)
        sentiment = LABELS[prediction_idx.item()]
        return SentimentResponse(
            sentiment=sentiment,
            confidence=confidence.item(),
        )


@router.post("/sentiment", response_model=SentimentResponse)
def analyze_sentiment(payload: SentimentRequest) -> SentimentResponse:
    return predict_sentiment(payload.text)

