# 10 - Document loader

## What is it?

Document loaders read data from a source and turn it into `Document` objects.
A `Document` has two parts: `page_content` (the text) and `metadata` (where it
came from). This example loads a tiny local text file.

## Flow

```
Text file
  ↓  TextLoader
Document (page_content + metadata)
```

## Code idea

`TextLoader("data/company.txt").load()` returns a list of Documents. Print
`page_content` and `metadata` to see the two parts.

## Important lines

```python
loader = TextLoader("data/company.txt")
documents = loader.load()
doc.page_content   # the text
doc.metadata       # source info
```

## Interview question

1. What is a Document in LangChain?
2. What does metadata contain?
3. Name a few loaders.

## Interview answer

1. A unit of text: `page_content` + `metadata`.
2. Info about the source, e.g. file path, URL, title.
3. TextLoader, PyPDFLoader, WebBaseLoader (thousands exist in langchain-community).

## Remember

- Loaders only READ data; they don't split or embed.
- `.load()` returns a list, because one file can produce many Documents.
- Metadata later enables filtering (project 16).
