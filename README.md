# AI Text Tools API

AI Text Tools API is a lightweight, CPU-friendly NLP microservice built with FastAPI. It provides essential text-processing and AI-powered features using efficient HuggingFace models and specific NLP libraries.

## Features

*   **Text Summarization**: Generate concise summaries using the **T5-small** model.
*   **Keyword Extraction**: Extract important keywords using **YAKE**.
*   **Sentiment Analysis**: Detect positive or negative sentiment using **DistilBERT** (SST-2).
*   **Text Cleaning Utilities**: Clean text by removing stopwords, punctuation, and extra whitespace with customizable options.

## Tech Stack

*   [FastAPI](https://fastapi.tiangolo.com/) for backend API development
*   [HuggingFace Transformers](https://huggingface.co/transformers/) for ML models (T5, DistilBERT)
*   [YAKE](https://github.com/LIAAD/yake) for keyword extraction
*   [Uvicorn](https://www.uvicorn.org/) as ASGI server
*   [uv](https://github.com/astral-sh/uv) for fast Python package management
*   Python 3.10+

## Folder Structure

```
D:/project/
├───.gitignore
├───README.md
├───requirements.txt
├───uv.lock
├───pyproject.toml
├───MAIN/
│   ├───main.py
│   ├───endpoints/
│   │   ├───clean_text.py
│   │   ├───keywords.py
│   │   ├───sentiment.py
│   │   └───summarization.py
│   └───schemas/
│       ├───text_request.py
│       └───text_response.py
```

## API Endpoints

| Endpoint      | Method | Description                               |
| ------------- | ------ | ----------------------------------------- |
| `/summarize`  | POST   | Generate a concise summary of input text  |
| `/keywords`   | POST   | Extract important keywords from text      |
| `/sentiment`  | POST   | Analyze sentiment (positive/negative) with confidence |
| `/clean`      | POST   | Clean and normalize text                  |

### Example Request

**POST** `/sentiment`

```json
{
  "text": "FastAPI is a modern, fast web framework for building APIs with Python."
}
```

### Example Response

```json
{
  "sentiment": "POSITIVE",
  "confidence": 0.9998
}
```

## Getting Started

### Prerequisites

*   Python 3.10 or higher
*   [Git](https://git-scm.com/)

### Installation

This project uses `uv` for package management, but also provides a `requirements.txt` for standard pip installation.

#### Option 1: Using pip

1.  Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ai-text-tools-api.git
    cd ai-text-tools-api
    ```

2.  Create a virtual environment:
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

#### Option 2: Using uv (Recommended)

1.  Install uv:
    ```bash
    pip install uv
    ```

2.  Sync dependencies:
    ```bash
    uv sync
    ```

### Running the Application

Start the server using Uvicorn:

```bash
uvicorn MAIN.main:app --reload
```

## Usage

Once the application is running, you can send POST requests to the API endpoints.

**Example: Summarization**

```bash
curl -X POST "http://127.0.0.1:8000/summarize" \
     -H "Content-Type: application/json" \
     -d '{"text": "Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals including humans.", "min_length": 10, "max_length": 50}'
```

**Example: Keyword Extraction**

```bash
curl -X POST "http://127.0.0.1:8000/keywords" \
     -H "Content-Type: application/json" \
     -d '{"text": "FastAPI is a modern, fast web framework for building APIs with Python.", "top_n": 3}'
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
