"""14 - Retriever: the interface that returns relevant documents.

Vector store  = stores and searches vectors.
Retriever     = the interface used to retrieve relevant documents
                for a query (it hides how the search happens).
"""

import os

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004",
    api_key=api_key,
)

docs = [
    Document(page_content="LangChain is a framework for LLM apps.", metadata={"topic": "ai"}),
    Document(page_content="Gemini is Google's language model.", metadata={"topic": "ai"}),
    Document(page_content="FastAPI is a Python web framework.", metadata={"topic": "python"}),
]

# 1. Vector store = stores and searches vectors
vector_store = FAISS.from_documents(docs, embeddings)

# 2. Retriever = the simple interface used to retrieve documents
#    as_retriever() wraps the store; k = how many documents to return.
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# 3. Query the retriever: query -> documents (no model involved)
results = retriever.invoke("Which framework helps build LLM apps?")

for doc in results:
    print(f"[{doc.metadata['topic']}] {doc.page_content}")
