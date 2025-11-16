from fastapi import FastAPI
import regex as re
from transformers import AutoModelForSeq2SeqLm, AutoTokenizer
import torch

app = FastAPI()

MODEL = "t5-small"

def preproduction_text(text:str)-> str:
    text = re.sub(r"[^a-zA-Z0-9\s]","",text)
    text = re.sub(r"\s+"," ",text)
    return text

def summarize_text(text:str) -> str:
    model = AutoModelForSeq2SeqLm.from_pretrained(MODEL)
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    
    preprocess_text = preproduction_text(text)
    text = tokenizer(preprocess_text,return_tensors="pt")

    with torch.no_grad():
        output = model.generate(text, max_length= 100, num_beams=5, early_stopping=True)
        summary = tokenizer.decode(output[0],skip_special_tokens=True)
        return summary

    
@app.post("/summarize")
def summarize_text(text:str) -> str:
    text = input("enter the text to summarize:")
    sentiment = summarize_text(text)
    return sentiment

