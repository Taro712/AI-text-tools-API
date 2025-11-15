# AI Text Tools API

AI Text Tools API is a lightweight, CPU-friendly NLP microservice built with FastAPI. It provides essential text-processing and AI-powered features using tiny HuggingFace models and classical NLP techniques. It can be deployed on free tier of railway.

## Features

*   **Text Summarization**: Generate concise summaries using DistilBART or T5-small.
*   **Keyword Extraction**: Extract important keywords using RAKE, YAKE, and other NLP techniques.
*   **Sentiment Analysis**: Detect positive, neutral, or negative sentiment using DistilBERT SST-2.
*   **Language Detection**: Identify the language of the input text using langdetect.
*   **Text Cleaning Utilities**: Clean text by removing HTML, stopwords, punctuation, and extra whitespace.

## Tech Stack

*   [FastAPI](https://fastapi.tiangolo.com/) for backend API development
*   [HuggingFace Transformers](https://huggingface.co/transformers/) for lightweight ML models
*   [NLTK](https://www.nltk.org/), [langdetect](https://pypi.org/project/langdetect/), and [scikit-learn](https://scikit-learn.org/stable/) for classical NLP utilities
*   [Uvicorn](https://www.uvicorn.org/) as ASGI server
*   [Render](https://render.com/), [Railway](https://railway.app/), or [Vercel](https://vercel.com/) for deployment
*   Python 3.10 or higher

## Folder Structure

```
D:/project/
├───.gitignore
├───README.md
├───requirements.txt
├───uv.lock
├───.git/...
├───.venv/...
└───MAIN/
    ├───config.py
    ├───main.py
    ├───core/
    ├───endpoints/
    └───schemas/
```

## API Endpoints

| Endpoint      | Method | Description                               |
| ------------- | ------ | ----------------------------------------- |
| `/summarize`  | POST   | Generate a concise summary of input text  |
| `/keywords`   | POST   | Extract important keywords from text      |
| `/sentiment`  | POST   | Analyze sentiment (positive, neutral, negative) |
| `/language`   | POST   | Detect input text language                |
| `/clean`      | POST   | Clean and normalize text                  |

**Example Request**

```json
{
  "text": "FastAPI is a modern, fast web framework for building APIs with Python."
}
```

**Example Response**

```json
{
  "summary": "FastAPI is a fast web framework for building APIs with Python.",
  "keywords": ["FastAPI", "web framework", "APIs", "Python"],
  "sentiment": "positive",
  "language": "en",
  "cleaned_text": "FastAPI modern fast web framework building APIs Python"
}
```

## Getting Started

### Prerequisites

*   Python 3.10 or higher
*   [Git](https://git-scm.com/)

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/yourusername/ai-text-tools-api.git
    cd ai-text-tools-api
    ```

2.  Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```

3.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Run the application:

    ```bash
    uvicorn MAIN.main:app --reload
    ```

## Usage

Once the application is running, you can send POST requests to the API endpoints. For example, you can use `curl` or any API client like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/).

```bash
curl -X POST "http://127.0.0.1:8000/summarize" -H "Content-Type: application/json" -d '{"text": "FastAPI is a modern, fast web framework for building APIs with Python."}'
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
