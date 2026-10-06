"""11 - Text splitter: cut long text into small overlapping chunks.

chunk_size   = max characters per chunk
chunk_overlap = characters shared between neighbouring chunks
               (keeps context that spans chunk borders)
"""

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Load one document (a small file with a few paragraphs)
doc = TextLoader("data/company.txt").load()[0]

# 2. Create the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,     # max characters per chunk
    chunk_overlap=20,   # overlap so meaning isn't cut in half
)

# 3. Split the document into smaller Documents
chunks = splitter.split_documents([doc])

print(f"Original length : {len(doc.page_content)} chars")
print(f"Number of chunks: {len(chunks)}")
print()

for i, chunk in enumerate(chunks):
    print(f"--- chunk {i + 1} ({len(chunk.page_content)} chars) ---")
    print(chunk.page_content)
    print()
