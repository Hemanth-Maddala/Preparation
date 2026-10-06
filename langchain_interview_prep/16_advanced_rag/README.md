# 16 - Advanced RAG

## What is it?

Basic RAG works, but retrieval quality limits the answer. Advanced RAG adds
small techniques around retrieval. This project shows three tiny patterns
separately; agentic RAG (a fourth pattern) lives in project 27.

## Flow

```
1) Query rewriting: question -> LLM rewrites -> retrieve
2) Metadata filter: similarity_search(..., filter={...})
3) Reranking: retrieve candidates -> re-sort by relevance -> take top k
```

## Code idea

1) A small `prompt | model` chain rewrites the question before retrieval.
2) `similarity_search` accepts a `filter` dict on metadata.
3) A rerank function re-sorts candidates (a real one uses an LLM/cross-encoder).

## Important lines

```python
rewritten = (rewrite_prompt | model).invoke({"question": question}).content
results = vector_store.similarity_search(q, k=1, filter={"product": "NovaDeploy"})
top = rerank(query, vector_store.similarity_search(query, k=4))[:2]
```

## Interview question

1. Name three advanced RAG techniques.
2. Why rewrite the query?
3. What is agentic RAG?

## Interview answer

1. Query rewriting, metadata filtering, reranking (also: hybrid search, parent
   documents, agentic retrieval).
2. Users type vague or abbreviated questions; a rewritten query retrieves better.
3. An agent decides WHEN and WHAT to retrieve, instead of always retrieving
   (see project 27).

## Remember

- Advanced RAG is a bag of small patterns, not one big app.
- Filters need good metadata at indexing time.
- Reranking is done AFTER a first broad retrieval.
