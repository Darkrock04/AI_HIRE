# Retrieval-Augmented Generation (RAG)

LLMs are frozen in time; they don't know your company's private data or recent news. RAG solves this by retrieving relevant documents from a database and injecting them into the prompt *before* the LLM answers.

## The RAG Pipeline:
1. **Document Loaders:** Connect to data sources (PDFs, URLs, Databases) and load them into LangChain `Document` objects.
2. **Text Splitters:** LLMs have context limits (e.g., 8k tokens). You cannot feed a 500-page PDF into an LLM. Text splitters chop the document into small, manageable chunks (e.g., 1000 characters each).
3. **Embeddings:** Convert text chunks into numerical vectors (arrays of numbers) that capture semantic meaning.
4. **Vector Stores:** A specialized database (like ChromaDB or FAISS) that stores these numerical vectors. It allows for blazing-fast similarity searches.

## Types of Retrieval
The final step is querying the data, which can be done in three ways:
1. **Dense Retrieval:** Uses numerical vectors (embeddings) to understand the *semantic meaning* of a query. Great for conceptual matching (e.g., matching "puppy" with "dog").
2. **Sparse Retrieval (BM25):** Uses traditional keyword matching. Great for exact matches like serial numbers or specific names where neural networks often fail.
3. **Hybrid Retrieval:** The industry standard. Uses an `EnsembleRetriever` to run both Dense and Sparse searches simultaneously, combining the results for the highest possible accuracy.
