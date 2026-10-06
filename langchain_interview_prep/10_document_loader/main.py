"""10 - Document loader: read a local text file into a Document.

A Document = page_content (the text) + metadata (source info).
No LLM needed for this step.
"""

from langchain_community.document_loaders import TextLoader

# 1. Create the loader pointing at a small text file
loader = TextLoader("data/company.txt")

# 2. Load: returns a list of Document objects
documents = loader.load()

print(f"Number of documents: {len(documents)}")

# 3. Inspect the Document
doc = documents[0]
print(f"page_content:\n{doc.page_content}")
print(f"metadata: {doc.metadata}")  # e.g. {'source': 'data/company.txt'}
