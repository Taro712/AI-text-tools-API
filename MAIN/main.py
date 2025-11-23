from fastapi import FastAPI
from MAIN.endpoints import clean_text, keywords, sentiment, summarization

app = FastAPI(
    title="AI Text Tools API",
    description="API for various AI-powered text processing tools.",
    version="1.0.0",
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Text Tools API!"}


app.include_router(clean_text.router, tags=["Clean Text"])
app.include_router(keywords.router, tags=["Keywords"])
app.include_router(sentiment.router, tags=["Sentiment"])
app.include_router(summarization.router, tags=["Summarization"])
