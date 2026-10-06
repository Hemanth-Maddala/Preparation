import os
from dotenv import load_dotenv

load_dotenv()

# Embedding model
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Chroma persist directory
CHROMA_PERSIST_DIR = "./chroma_db"

# Collection name
CHROMA_COLLECTION = "rag_documents"

# LLM settings
TEMPERATURE = 0.3
MAX_TOKENS = 1024

# Text splitter settings
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Retrieval settings
TOP_K = 3