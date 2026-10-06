"""16 - Advanced RAG: three small patterns, shown separately.

1. Query rewriting: improve the question BEFORE retrieval.
2. Metadata filtering: restrict the search to matching metadata.
3. Reranking concept: re-sort retrieved candidates by relevance.

(Agentic RAG - the 4th pattern - is covered in project 27.)
"""

import os

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise SystemExit("Set GEMINI_API_KEY in a .env file (copy .env.example to .env)")

model = ChatGoogleGenerativeAI(
    model=os.getenv("GEMINI_MODEL", "gemini-3.5-flash"),
    api_key=api_key,
)
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", api_key=api_key)

docs = [
    Document(page_content="NovaDeploy deploys cloud applications.", metadata={"product": "NovaDeploy"}),
    Document(page_content="NovaMetrics monitors server health.", metadata={"product": "NovaMetrics"}),
    Document(page_content="NovaDocs generates API documentation.", metadata={"product": "NovaDocs"}),
    Document(page_content="Gemini is a family of language models by Google.", metadata={"topic": "ai"}),
]
vector_store = FAISS.from_documents(docs, embeddings)


# ---------- Pattern 1: query rewriting ----------
def rewrite_question(question: str) -> str:
    prompt = ChatPromptTemplate.from_messages([
        ("human", "Rewrite this search query to be clearer: {question}"),
    ])
    return (prompt | model).invoke({"question": question}).content


print("1) Query rewriting (improve the query before retrieving)")
question = "how do I write docs for my api?"
rewritten = rewrite_question(question)
print(f"   before: {question}")
print(f"   after : {rewritten}")
print(f"   retrieved: {vector_store.similarity_search(rewritten, k=1)[0].page_content}")

# ---------- Pattern 2: metadata filtering ----------
print("\n2) Metadata filtering (restrict search to a subset)")
results = vector_store.similarity_search(
    "which tool deploys apps?", k=1, filter={"product": "NovaDeploy"}
)
for d in results:
    print(f"   only {d.metadata['product']}: {d.page_content}")

# ---------- Pattern 3: reranking concept ----------
# Retrieval returns a candidate list; a reranker re-sorts it by relevance.
# Real systems use an LLM or a cross-encoder. Here: a simple keyword score.


def rerank(query: str, documents):
    scored = [
        (doc, sum(q.lower() in doc.page_content.lower() for q in query.split()))
        for doc in documents
    ]
    return [doc for doc, _ in sorted(scored, key=lambda t: t[1], reverse=True)]


print("\n3) Reranking concept (re-sort candidates by relevance)")
candidates = vector_store.similarity_search("product", k=4)
for d in rerank("deploy", candidates):
    print(f"   {d.page_content}")
