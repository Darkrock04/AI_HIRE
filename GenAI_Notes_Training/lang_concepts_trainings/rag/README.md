# Retrieval-Augmented Generation (RAG) Concepts

Welcome to the **RAG** module! RAG is currently the most important architecture in Enterprise AI. It allows Large Language Models (LLMs) to answer questions based on your private data without requiring expensive model fine-tuning.

Before looking at the implementation code, please read this theoretical guide to understand how RAG works under the hood.

---

## 🧠 What is RAG?
Large Language Models have a "knowledge cutoff" (they don't know the news from yesterday) and they do not have access to your private company documents. If you ask an LLM "What is my company's refund policy?", it will hallucinate.

**Retrieval-Augmented Generation (RAG)** solves this by adding a "Search Engine" to the LLM. 
1. **Retrieve:** When a user asks a question, we first search your private documents for the answer.
2. **Augment:** We take the retrieved paragraphs and paste them directly into the LLM's prompt.
3. **Generate:** The LLM reads those paragraphs and generates a final, accurate answer.

---

## ⚙️ The 5 Steps of a RAG Pipeline

To build a RAG application, you must process your data through these 5 steps:

### 1. Document Loaders
You cannot feed raw PDFs or HTML into an LLM. You first need to extract the raw text. Document Loaders take files (PDF, CSV, HTML, Notion, Slack) and convert them into standard Text Documents.

### 2. Text Splitters (Chunking)
LLMs have a "context window" limit (they can only read a certain number of words at a time). If you have a 500-page PDF, you cannot pass the whole thing to the LLM. 
Text Splitters chop your large documents into small "Chunks" (e.g., 1000 characters per chunk). 
*Note: You must ensure chunks have "Overlap" so you don't accidentally cut a sentence in half!*

### 3. Embeddings (Vectorization)
This is the most critical concept. How does a computer know that the word "Dog" is similar to the word "Puppy"? 
An Embedding model converts your text chunks into massive arrays of numbers (Vectors). If two paragraphs have similar meanings, their numbers will be close together in a multi-dimensional space.

### 4. Vector Databases
Once all your chunks are converted into Vectors, you need somewhere to store them. 
A Vector Store (like ChromaDB, FAISS, or Pinecone) is a special database optimized for searching numbers instead of text.

### 5. Retrievers
When a user asks a question, the question is also converted into a Vector. The Retriever searches the Vector Database for the chunks whose numbers are closest to the question's numbers. It returns the top 3 or 4 most relevant chunks.

---

## 🚀 Advanced RAG Techniques

Basic RAG works well, but it can fail if the user asks a tricky question. In `02_advanced_rag_techniques.ipynb`, we cover ways to improve accuracy:

*   **Multi-Query Retrieval:** The LLM rewrites the user's question in 5 different ways to ensure we don't miss any relevant documents in the database.
*   **Parent-Document Retrieval:** Instead of returning a small chunk to the LLM, we return the entire page the chunk came from, giving the LLM more context.
*   **Reranking:** We retrieve 20 documents, and then use a separate "Reranker" AI model to score and re-order them from most to least relevant before passing them to the main LLM.

---

Now that you understand the theory, open `01_basic_rag_pipeline.ipynb` to build your first RAG application from scratch!
