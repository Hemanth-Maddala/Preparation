"""13 - Vector store: store documents as vectors and search by similarity.

FAISS runs locally in memory: documents -> embeddings -> index.
similarity_search() finds the nearest documents to a query.
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

# 1. A few tiny documents with metadata
docs = [
    Document(page_content="LangChain builds LLM applications.", metadata={"category": "ai"}),
    Document(page_content="Pandas is a Python data library.", metadata={"category": "python"}),
    Document(page_content="React is a JavaScript UI library.", metadata={"category": "js"}),
]

# 2. Embed the documents and store them in a local index
vector_store = FAISS.from_documents(docs, embeddings)

# 3. add_documents(): add more documents after the store exists
vector_store.add_documents([
    Document(page_content="NumPy adds arrays to Python.", metadata={"category": "python"}),
])

# 4. similarity_search(): find documents closest to the query
results = vector_store.similarity_search(
    "Which library works with arrays in Python?", k=2
)

for doc in results:
    print(f"[{doc.metadata['category']}] {doc.page_content}")
