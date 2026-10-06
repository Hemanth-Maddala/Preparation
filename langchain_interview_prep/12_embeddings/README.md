# 12 - Embeddings

## What is it?

An embedding model converts text into a vector (a list of numbers) that captures
the meaning of the text. Texts that mean the same thing end up close together in
vector space. This step needs no vector database.

## Flow

```
Text
  ↓  GoogleGenerativeAIEmbeddings
Vector (list of floats)
```

## Code idea

`embed_query(text)` returns the vector. Its length is the number of dimensions
the model uses. Every chunk of a RAG pipeline gets embedded the same way.

## Important lines

```python
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004", api_key=api_key)
vector = embeddings.embed_query(text)
len(vector)  # number of dimensions
```

## Interview question

1. What is an embedding?
2. What does the vector represent?
3. Embedding vs tokenization: difference?

## Interview answer

1. A list of numbers representing a text's meaning.
2. The position of that text in "semantic space"; similar texts are near each other.
3. Tokens are the raw text pieces the LLM reads; embeddings are numerical
   representations used to compare/retrieve text.

## Remember

- Embedding model, not an LLM; no answers, only vectors.
- The same embedding model must be used for indexing and querying.
- Similarity = distance between vectors (cosine).
