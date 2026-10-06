"""
STEP 15: RAG CODING PRACTICE
============================
15 coding tasks, progressively harder.
Try each one. Check the solution when ready.
"""

# ============================================
# LEVEL 1: Basics
# ============================================

# Task 1: Load a document
# Write code to load data/sample.txt using TextLoader
# Print the number of documents loaded

# YOUR CODE HERE:


# Task 2: Split into chunks
# Split the loaded document into chunks
# Use chunk_size=300, chunk_overlap=30
# Print the number of chunks

# YOUR CODE HERE:


# Task 3: Create embeddings
# Create HuggingFaceEmbeddings with all-MiniLM-L6-v2
# Embed the sentence "Acme was founded in 1985"
# Print the dimension of the embedding

# YOUR CODE HERE:


# Task 4: Create Chroma store
# Create a Chroma vector store from the chunks
# Print the number of documents in the store

# YOUR CODE HERE:


# Task 5: Similarity search
# Search for "When was Acme founded?"
# Return top 2 results
# Print the content of each result

# YOUR CODE HERE:


# ============================================
# LEVEL 2: Building the Pipeline
# ============================================

# Task 6: Create a retriever
# Convert the vector store to a retriever
# Use k=2
# Invoke with "What products does Acme sell?"
# Print the retrieved documents

# YOUR CODE HERE:


# Task 7: Add an LLM
# Initialize ChatOllama with model="tinyllama"
# Invoke with "What is 2+2?"
# Print the response

# YOUR CODE HERE:


# Task 8: Create a RAG prompt
# Create a ChatPromptTemplate that:
# - Takes context and question
# - Tells the LLM to answer based on context
# Print the input variables

# YOUR CODE HERE:


# Task 9: Connect retriever + LLM
# Build a chain that:
# 1. Retrieves documents
# 2. Formats them as context
# 3. Fills the prompt
# 4. Calls the LLM
# 5. Returns the answer
# Test with "When was Acme founded?"

# YOUR CODE HERE:


# Task 10: Return source documents
# Modify the chain to return:
# - The answer
# - The source documents used
# Print both

# YOUR CODE HERE:


# ============================================
# LEVEL 3: Advanced
# ============================================

# Task 11: Add metadata filtering
# Search only in documents with source="data/sample.txt"
# Hint: Use filter parameter in similarity_search

# YOUR CODE HERE:


# Task 12: Change top-k
# Compare results with k=1, k=3, k=5
# Print how many results you get for each

# YOUR CODE HERE:


# Task 13: Handle no relevant documents
# Create a function that:
# - Retrieves documents
# - If no documents found, return "No relevant info"
# - Otherwise, return the answer
# Test with a query not in the documents

# YOUR CODE HERE:


# Task 14: Add conversation history
# Modify the chain to:
# - Accept a list of (question, answer) pairs
# - Include history in the prompt
# Test with 2 questions

# YOUR CODE HERE:


# Task 15: Convert to FastAPI endpoint
# Create a FastAPI app with:
# - POST /ask endpoint
# - Accepts {"question": "..."}
# - Returns {"answer": "...", "sources": [...]}
# Test it with curl or requests

# YOUR CODE HERE: