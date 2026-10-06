# 11 - Text splitter

## What is it?

`RecursiveCharacterTextSplitter` cuts a long document into smaller chunks so each
fits into the model context and retrieval finds the right part. The most common
splitter in RAG.

## Flow

```
Document
  ↓  RecursiveCharacterTextSplitter(chunk_size, chunk_overlap)
chunks (many small Documents)
```

## Code idea

`split_documents([doc])` returns chunk Documents. `chunk_size` is the maximum
size; `chunk_overlap` keeps a few characters from the previous chunk so sentences
and meaning survive the cut.

## Important lines

```python
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
chunks = splitter.split_documents([doc])
```

## Interview question

1. Why split documents at all?
2. What do chunk_size and chunk_overlap mean?
3. Why use overlap?

## Interview answer

1. Documents are too long for the model context, and retrieval works better on
   small focused pieces.
2. chunk_size = max size of a chunk; chunk_overlap = shared text between chunks.
3. So context that crosses the boundary of two chunks is not lost.

## Remember

- Split AFTER loading, BEFORE embedding.
- RecursiveCharacterTextSplitter tries separators from big to small.
- chunk_size + chunk_overlap control the quality/size trade-off.
