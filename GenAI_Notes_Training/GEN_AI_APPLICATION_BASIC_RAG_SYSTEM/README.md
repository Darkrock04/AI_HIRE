# Basic RAG Application

This is a modern, simplified Generative AI application featuring a straightforward Retrieval-Augmented Generation (RAG) architecture, built with a Streamlit frontend and a FastAPI backend.

## Features
- **Basic RAG Architecture**:
  - **Retrieve -> Prompt -> Answer** flow.
  - No complex multi-agent routing or planning overhead.
- **Vector Database**:
  - Uses ChromaDB for local vector storage.
  - Supports Text and PDF ingestion with automatic chunking.
- **Dual Model Support (via `.env`)**:
  - Built-in support for **NVIDIA** (cloud APIs) and **Self-Hosted** (local/HuggingFace) providers.
  - Automatically handles asymmetric embedding models (e.g., `nvidia/nv-embedqa-e5-v5`).
- **Memory**:
  - Frontend passes the last 10 messages so the model remembers conversation history.

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**:
   Edit the `.env` file and set up your API keys and endpoint URLs. 
   You can easily toggle between `nvidia` and `self_hosted` using `ACTIVE_CHAT_PROVIDER` and `ACTIVE_EMBED_PROVIDER`.

3. **Start the Backend (FastAPI)**:
   ```bash
   uvicorn backend.main:app --reload
   ```

4. **Start the Frontend (Streamlit)**:
   Open a new terminal and run:
   ```bash
   streamlit run frontend/app.py
   ```

## Architecture Flow
1. User uploads a document via Streamlit.
2. FastAPI backend chunks it, embeds it, and stores it in a session-unique ChromaDB collection.
3. User submits a chat request.
4. Backend retrieves the top-4 most relevant chunks from ChromaDB.
5. The conversation history, retrieved context, and the user's question are formatted into a single prompt.
6. The LLM generates and returns the final answer directly to the user.
