from fastapi import FastAPI
import regex as re
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

app = FastAPI()

MODEL = "distilbert-base-uncased-finetuned-sst-2-english"

def preproduction_text(text:str)-> str:
    text = re.sub(r"[^a-zA-Z0-9\s]","",text)
    text = re.sub(r"\s+"," ",text)
    return text

def extract_keywords(text:str)-> list[str]:
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    
    preprocess_text = preproduction_text(text)
    text = tokenizer(preprocess_text,return_tensors="pt")

    with torch.no_grad():
      output = model(**text)
      Logits = output.logits
      predictions = torch.argmax(Logits,dim=-1)
      return predictions.item()

@app.post("/sentiment")
def analyze_sentiment(text:str) -> str:
    text = input("enter the text to analyze:")
    sentiment = extract_keywords(text)
    return sentiment

