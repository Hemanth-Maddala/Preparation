# 14 - Retriever

## What is it?

A retriever is the interface that returns relevant documents for a query. The
vector store is one way to power it; a retriever could also be keyword search or
a hybrid. This is why RAG code talks to a retriever, not the store directly.

## Flow

```
Vector store
  ↓  as_retriever(k=2)
Retriever
  ↓  invoke(query)
Relevant documents
```

## Code idea

`vector_store.as_retriever(search_kwargs={"k": 2})` creates a retriever. Then
`retriever.invoke(query)` returns the top-k Documents. No LLM is involved.

## Important lines

```python
vector_store = FAISS.from_documents(docs, embeddings)
retriever = vector_store.as_retriever(search_kwargs={"k": 2})
results = retriever.invoke("query")
```

## Interview question

1. Vector store vs retriever?
2. What does a retriever return?
3. Why is the retriever a separate concept?

## Interview answer

1. The store holds and searches vectors; the retriever is the interface that
   returns documents for a query (any search backend can power it).
2. A list of `Document` objects.
3. So you can swap the search backend (vector, keyword, hybrid) without changing
   the rest of the pipeline.

## Remember

- `as_retriever()` converts a vector store into a retriever.
- Retrievers return Documents, not strings.
- RAG pipelines use the retriever, not the store directly.
