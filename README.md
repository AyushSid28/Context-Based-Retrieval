# Context-Based Retrieval System

A Retrieval-Augmented Generation (RAG) implementation using LangChain for context-aware question answering from web documentation.

This project implements a complete RAG pipeline that ingests web content, processes it into searchable chunks, and provides contextual answers to user queries using OpenAI's language models.

The system follows a standard RAG architecture: data ingestion, text processing, embedding generation, vector storage, and query processing with retrieval chains.

## Installation

```bash
git clone https://github.com/AyushSid28/Context-Based-Retrieval.git
cd Context-Based-Retrieval
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a .env file with:
```
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_project_name
LANGCHAIN_TRACING_V2=true
```

## Usage

```bash
jupyter notebook Langchain/Project/GENAIApp.ipynb
```

The main implementation is in `Langchain/Project/GENAIApp.ipynb` which contains the complete RAG system with web data ingestion, text chunking, embedding generation, vector storage, and retrieval chains.

