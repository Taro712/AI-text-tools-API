# AI Text Tools API

AI Text Tools API is a lightweight, CPU-friendly NLP microservice built with FastAPI.  
It provides essential text-processing and AI-powered features using tiny HuggingFace models and classical NLP techniques.  
It can be deployed on free tier of railway

## Features

**Text Summarization**  
Generate concise summaries using DistilBART or T5-small.

**Keyword Extraction**  
Extract important keywords using RAKE, YAKE, and other NLP techniques.

**Sentiment Analysis**  
Detect positive, neutral, or negative sentiment using DistilBERT SST-2.

**Language Detection**  
Identify the language of the input text using langdetect.

**Text Cleaning Utilities**  
Clean text by removing HTML, stopwords, punctuation, and extra whitespace.

## Tech Stack

FastAPI for backend API development  
HuggingFace Transformers for lightweight ML models  
NLTK, langdetect, and scikit-learn for classical NLP utilities  
Uvicorn as ASGI server  
Render, Railway, or Vercel for deployment  
Python 3.10 or higher

## Folder Structure

ai-text-tools-api/
app/
main.py
config.py
router/
summarize.py
keywords.py
sentiment.py
language.py
clean.py
core/
model_loader.py
utils.py
schemas/
text_request.py
text_response.py
requirements.txt
.gitignore
README.md
Procfile
runtime.txt
start.sh
## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /summarize | POST | Generate a concise summary of input text |
| /keywords | POST | Extract important keywords from text |
| /sentiment | POST | Analyze sentiment (positive, neutral, negative) |
| /language | POST | Detect input text language |
| /clean | POST | Clean and normalize text |

**Example Request**

```json
{
  "text": "FastAPI is a modern, fast web framework for building APIs with Python."
}
Example Response

**json**

{
  "summary": "FastAPI is a fast web framework for building APIs with Python.",
  "keywords": ["FastAPI", "web framework", "APIs", "Python"],
  "sentiment": "positive",
  "language": "en",
  "cleaned_text": "FastAPI modern fast web framework building APIs Python"
}
**Installation**
git clone https://github.com/yourusername/ai-text-tools-api.git
cd ai-text-tools-api
Create a virtual environment

**bash**
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install dependencies

**bash**
pip install -r requirements.txt
Run the app locally

**bash**
uvicorn app.main:app --reload
**Use Cases**
Automating article or report summaries
Keyword extraction for blogs, SEO, or marketing
Sentiment analysis for reviews, social media, or feedback
Language detection for preprocessing pipelines
Lightweight backend microservice for SaaS or freelance projects