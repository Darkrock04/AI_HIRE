# Retrieval-Augmented Generation (RAG)

LLMs are frozen in time; they don't know your company's private data or recent news. RAG solves this by retrieving relevant documents from a database and injecting them into the prompt *before* the LLM answers.

## The RAG Pipeline:
1. **Document Loaders:** Connect to data sources (PDFs, URLs, Databases) and load them into LangChain `Document` objects.
2. **Text Splitters:** LLMs have context limits (e.g., 8k tokens). You cannot feed a 500-page PDF into an LLM. Text splitters chop the document into small, manageable chunks (e.g., 1000 characters each).
3. **Embeddings:** Convert text chunks into numerical vectors (arrays of numbers) that capture semantic meaning.
4. **Vector Stores:** A specialized database (like ChromaDB or FAISS) that stores these numerical vectors. It allows for blazing-fast similarity searches.
5. **Retrievers:** The interface that takes a user's question, embeds it, searches the Vector Store for the most mathematically similar chunks, and returns them.
