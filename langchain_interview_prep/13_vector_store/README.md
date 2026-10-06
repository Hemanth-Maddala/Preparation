# 13 - Vector store

## What is it?

A vector store embeds documents and keeps the vectors in an index. When you
search, it returns the documents whose vectors are closest to the query vector
(similarity search). FAISS is a local, in-memory store.

## Flow

```
Documents
  ↓  embeddings
Vector store (index)
  ↓  similarity_search(query)
Matching documents
```

## Code idea

`FAISS.from_documents(docs, embeddings)` creates the store. `add_documents()` adds
more. `similarity_search(query, k=n)` returns the n most similar documents.

## Important lines

```python
vector_store = FAISS.from_documents(docs, embeddings)
vector_store.add_documents(new_docs)
results = vector_store.similarity_search("query", k=2)
```

## Interview question

1. What does a vector store do?
2. What is k in similarity_search?
3. FAISS vs Chroma vs Pinecone?

## Interview answer

1. Stores embeddings and returns the closest documents to a query.
2. The number of results returned.
3. Same abstraction, different backends: FAISS/Chroma local, Pinecone hosted.
   Swapping them only changes the import.

## Remember

- A vector store needs the SAME embedding model used at query time.
- `similarity_search` returns `Document`s (text + metadata).
- It is storage + search; it does not answer questions.
