# LangChain RAG (Retrieval-Augmented Generation) Project

A comprehensive implementation of RAG using LangChain to create a context-based question-answering system that can retrieve and generate responses from web documentation.

## 🚀 Project Overview

This project demonstrates a complete RAG pipeline that:
- **Ingests data** from web sources (LangChain documentation)
- **Processes and chunks** text for optimal retrieval
- **Creates embeddings** and stores them in a vector database
- **Retrieves relevant context** for user queries
- **Generates answers** using OpenAI's GPT models

## 📁 Project Structure

```
Langchain/
├── Project/
│   └── GENAIApp.ipynb          # Main RAG implementation
├── DataIngestion/
│   ├── Data_Ingestion.ipynb    # Web scraping and data loading
│   ├── attention.pdf           # Sample PDF document
│   └── speech.txt              # Sample text file
├── Embeddings/
│   ├── embedding.ipynb         # OpenAI embeddings
│   ├── HuggingfaceEmbedding.ipynb
│   └── ollamaembedding.ipynb
├── vector_store/
│   ├── FAISS.ipynb            # FAISS vector store implementation
│   └── Chroma.ipynb           # ChromaDB vector store implementation
├── Data Transformer/
│   └── Text-Splitting.ipynb   # Text chunking strategies
├── requirements.txt            # Project dependencies
└── Started.ipynb             # Getting started guide
```

## 🛠 Features

- **Web Data Ingestion**: Scrapes content from websites using WebBaseLoader
- **Text Processing**: Intelligent text chunking with RecursiveCharacterTextSplitter
- **Vector Storage**: FAISS integration for efficient similarity search
- **Multiple Embeddings**: Support for OpenAI, HuggingFace, and Ollama embeddings
- **Question Answering**: Context-aware responses using retrieval chains
- **LangChain Integration**: Built with LangChain 1.0 and classic chains

## 🔧 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Langchain
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with:
```
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_project_name
```

## 🚀 Usage

### Main RAG Application
Open and run `Project/GENAIApp.ipynb` to see the complete RAG implementation:

1. **Data Ingestion**: Loads content from LangChain documentation
2. **Text Chunking**: Splits documents into manageable chunks
3. **Embedding Creation**: Generates embeddings using OpenAI
4. **Vector Storage**: Stores embeddings in FAISS vector database
5. **Question Answering**: Retrieves context and generates responses

### Example Queries
- "What is integration stuff here?"
- "What is Vertex AI Model Garden and what packages are required?"

## 📚 Key Components

### Data Processing Pipeline
- **WebBaseLoader**: Scrapes web content
- **RecursiveCharacterTextSplitter**: Intelligently chunks text
- **OpenAIEmbeddings**: Creates semantic embeddings

### Vector Storage
- **FAISS**: Facebook AI Similarity Search for efficient retrieval
- **ChromaDB**: Alternative vector database option

### Language Models
- **OpenAI GPT-4o-mini**: Primary language model for generation
- **HuggingFace Models**: Alternative embedding options

## 🔄 RAG Workflow

1. **Ingest** → Load documents from web sources
2. **Transform** → Split text into chunks with overlap
3. **Embed** → Create vector representations
4. **Store** → Save embeddings in vector database
5. **Retrieve** → Find relevant chunks for queries
6. **Generate** → Create contextual responses

## 📋 Requirements

```
langchain==1.0.0
langchain-community==0.4
langchain-classic==1.0.0
langchain-openai==1.0.0
langchain-text-splitters==1.0.0
python-dotenv
faiss-cpu
chromadb
sentence-transformers
```

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new data sources
- Implementing additional embedding models
- Improving the retrieval accuracy
- Adding new vector store options

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [LangChain](https://langchain.com/)
- Powered by [OpenAI](https://openai.com/)
- Vector search by [FAISS](https://github.com/facebookresearch/faiss)
