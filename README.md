# Context-Based Retrieval System

A Retrieval-Augmented Generation (RAG) implementation using LangChain for context-aware question answering from web documentation.

## Project Overview

This project implements a complete RAG pipeline that ingests web content, processes it into searchable chunks, and provides contextual answers to user queries using OpenAI's language models.

## Core Features

1. Web data ingestion from documentation sources
2. Intelligent text chunking with overlap for context preservation
3. Vector embeddings using OpenAI's embedding models
4. FAISS vector database for efficient similarity search
5. Context-aware response generation using GPT-4o-mini
6. Retrieval chain implementation for seamless query processing

## Architecture

The system follows a standard RAG architecture:

1. **Data Ingestion**: WebBaseLoader scrapes content from target websites
2. **Text Processing**: RecursiveCharacterTextSplitter divides content into manageable chunks
3. **Embedding Generation**: OpenAI embeddings create vector representations
4. **Vector Storage**: FAISS stores embeddings for fast retrieval
5. **Query Processing**: Retrieval chain finds relevant context and generates responses

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AyushSid28/Context-Based-Retrieval.git
cd Context-Based-Retrieval
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create a .env file with:
```
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_project_name
LANGCHAIN_TRACING_V2=true
```

## Usage

Open and run the main notebook:
```bash
jupyter notebook Langchain/Project/GENAIApp.ipynb
```

The notebook contains the complete implementation with the following cells:

1. Environment setup and API key configuration
2. Web data ingestion using WebBaseLoader
3. Text chunking with RecursiveCharacterTextSplitter
4. OpenAI embedding generation
5. FAISS vector store creation
6. Similarity search testing
7. Language model initialization
8. Retrieval chain setup
9. Document chain testing
10. Full retrieval chain implementation

## Example Queries

The system can answer questions about the ingested documentation:
- "What is integration stuff here?"
- "What is Vertex AI Model Garden and what packages are required?"

## Technical Stack

- **LangChain 1.0.0**: Framework for LLM applications
- **OpenAI GPT-4o-mini**: Language model for response generation
- **OpenAI Embeddings**: Text vectorization
- **FAISS**: Vector similarity search
- **Python 3.13**: Runtime environment
- **Jupyter**: Development environment

## Dependencies

```
langchain==1.0.0
langchain-community==0.4
langchain-classic==1.0.0
langchain-openai==1.0.0
langchain-text-splitters==1.0.0
langchain-core==1.0.0
python-dotenv
faiss-cpu
```

## Project Structure

```
Context-Based-Retrieval/
├── Langchain/
│   └── Project/
│       └── GENAIApp.ipynb    # Main RAG implementation
├── requirements.txt          # Project dependencies
├── README.md                # Project documentation
└── .gitignore               # Git ignore rules
```

## Implementation Details

The RAG system uses LangChain's classic chains for compatibility with existing workflows:

- **Document Chain**: Processes retrieved context with user queries
- **Retrieval Chain**: Combines document retrieval with response generation
- **Vector Store**: FAISS implementation for production-ready similarity search
- **Prompt Template**: Structured prompts for consistent response formatting

## Performance Considerations

- Chunk size: 1000 characters with 200 character overlap
- Vector dimensions: 1536 (OpenAI ada-002 embeddings)
- Retrieval method: Similarity search with configurable result count
- Response generation: Context-limited to prevent token overflow

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes and test thoroughly
4. Submit a pull request with detailed description

## License

This project is available under the MIT License.

## Contact

For questions or support, please open an issue in the GitHub repository.