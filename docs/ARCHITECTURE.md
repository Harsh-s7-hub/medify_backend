# Medify AI Backend Documentation

## Overview

The Medify AI Backend is a comprehensive system designed to provide medical AI assistance. It includes components for inference, retrieval, and a web API. This documentation provides a detailed overview of the system's architecture, components, and setup instructions.

## Architecture

The Medify AI Backend is built using Python and FastAPI. It consists of the following main components:

1. **app.py**: The main FastAPI application that handles HTTP requests.
2. **inference.py**: Contains the inference logic using the Groq API.
3. **rag_engine.py**: Manages the retrieval of context using a FAISS index.

## Components

### app.py

**Purpose**: The main FastAPI application that handles HTTP requests.

**Endpoints**:
- **GET /**: Returns a simple message indicating that the backend is running.
- **GET /health**: Returns the health status of the backend.
- **POST /chat**: Receives a user question, retrieves context, and generates a response.

**Dependencies**:
- `fastapi`: The web framework.
- `pydantic`: Data validation and settings management using Python type annotations.

**Example Usage**:
```bash
curl -X POST "http://localhost:10000/chat" -H "Content-Type: application/json" -d '{"question": "What are the symptoms of flu?"}'
```

### inference.py

**Purpose**: Contains the inference logic using the Groq API.

**Functions**:
- `generate_answer(prompt)`: Generates a response to a given prompt using the Groq API.

**Dependencies**:
- `groq`: The Groq API client.

**Example Usage**:
```python
from inference import generate_answer

prompt = "What are the symptoms of flu?"
response = generate_answer(prompt)
print(response)
```

### rag_engine.py

**Purpose**: Manages the retrieval of context using a FAISS index.

**Functions**:
- `retrieve_context(query, top_k=3)`: Retrieves the top-k context documents for a given query.

**Dependencies**:
- `faiss`: The FAISS library for similarity search.
- `sentence_transformers`: The Sentence Transformers library for embedding generation.

**Example Usage**:
```python
from rag_engine import retrieve_context

query = "What are the symptoms of flu?"
context = retrieve_context(query)
print(context)
```

## Setup Instructions

### Prerequisites

- Python 3.10
- Docker (optional, for containerized deployment)

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-repo/medify-ai-backend.git
    cd medify-ai-backend
    ```

2. **Create a Virtual Environment** (optional):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Download Cache Files**:
    The cache files are automatically downloaded when the application starts.

### Running Locally

1. **Start the Application**:
    ```bash
    uvicorn app:app --host 0.0.0.0 --port 10000
    ```

2. **Access the API**:
    Open a web browser and navigate to `http://localhost:10000/docs` to access the interactive API documentation.

### Containerized Deployment

1. **Build the Docker Image**:
    ```bash
    docker build -t medify-backend .
    ```

2. **Run the Docker Container**:
    ```bash
    docker run -p 7860:7860 medify-backend
    ```

3. **Access the API**:
    Open a web browser and navigate to `http://localhost:7860/docs` to access the interactive API documentation.

## Configuration

The backend can be configured using environment variables. The following variables are used:

- `GROQ_API_KEY`: The API key for the Groq API.
- `MODEL_NAME`: The name of the Groq model to use.

These variables can be set in a `.env` file or passed as environment variables when running the application.

## Error Handling

The backend includes basic error handling for API requests and file downloads. Errors are returned as JSON responses with appropriate status codes.

## Security Considerations

- **API Key Management**: The `GROQ_API_KEY` should be kept secure and not exposed in the codebase.
- **Input Validation**: The `ChatRequest` model ensures that the input question is not empty.
- **Output Sanitization**: The generated responses are sanitized to ensure they are safe and medically relevant.

## Deployment

The backend can be deployed using Docker for containerized environments. The `Dockerfile` provides instructions for building and running the application in a Docker container.

## Troubleshooting

- **Check Logs**: Review the application logs for any errors or warnings.
- **Verify Dependencies**: Ensure all dependencies are installed correctly.
- **Network Issues**: Ensure that the backend can access the Groq API and download cache files.

## Limitations

- **Cache Size**: The cache size is limited by the available disk space.
- **Performance**: The performance may be affected by the size of the corpus and the number of concurrent requests.

## Future Improvements

- **Scalability**: Implement load balancing and horizontal scaling for high traffic.
- **Real-time Updates**: Add support for real-time updates to the corpus and embeddings.
- **User Authentication**: Implement user authentication and authorization.

## Conclusion

The Medify AI Backend is a robust system for providing medical AI assistance. It includes components for inference, retrieval, and a web API. This documentation provides a detailed overview of the system's architecture, components, and setup instructions.