"""
STEP 14: YOUR TURN
==================
Write a RAG pipeline from scratch.

Requirements:
1. Load a text file using TextLoader
2. Split into chunks (chunk_size=500, chunk_overlap=50)
3. Create embeddings using HuggingFaceEmbeddings
4. Create a Chroma vector store
5. Create a retriever
6. Create a prompt template
7. Build a chain using LCEL
8. Invoke the chain with a question

DO NOT look at the solution below.
Write your code in a separate file first.

When ready, check the solution below.
"""

# YOUR CODE HERE:
# Write your RAG pipeline in a file called my_rag.py


# ============================================
# SOLUTION (Try to write it first!)
# ============================================

"""
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def format_docs(docs):
    return "\\n\\n".join(d.page_content for d in docs)


# Load
docs = TextLoader("data/sample.txt").load()

# Split
chunks = RecursiveCharacterTextSplitter(
    chunk_size=500, chunk_overlap=50
).split_documents(docs)

# Embed + Vector Store
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectorstore = Chroma.from_documents(chunks, embeddings)

# Retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# LLM
llm = ChatOllama(model="tinyllama")

# Prompt
prompt = ChatPromptTemplate.from_template(
    "Answer based on context:\\n{context}\\n\\nQuestion: {question}\\n\\nAnswer:"
)

# Chain
chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt | llm | StrOutputParser()
)

# Invoke
print(chain.invoke("When was Acme founded?"))
"""