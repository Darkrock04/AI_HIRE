# Generative AI & LangChain Concepts

**Generative AI (GenAI)** refers to algorithms (such as Large Language Models or LLMs) that can generate text, code, or other content based on the data they were trained on. To build robust applications around these models, we use frameworks like **LangChain** and **LangGraph**.

## 1. Core Framework: LangChain

LangChain is a framework designed to simplify the creation of applications using LLMs. It provides standard interfaces for:
*   **Models:** Connecting to LLM providers (e.g., OpenAI, Groq, HuggingFace).
*   **Prompts:** Managing and formatting inputs to the models dynamically.
*   **Memory:** Giving LLMs the ability to remember past conversation turns, which is essential for chatbots.
*   **Chains:** Linking together multiple components (like a prompt + an LLM) into a single, cohesive workflow.

## 2. Retrieval-Augmented Generation (RAG)

LLMs have a knowledge cutoff and cannot access your private data natively. **RAG** solves this by:
1.  **Ingestion:** Loading documents (PDFs, text files), chunking them into smaller pieces, and converting them into mathematical vectors (Embeddings).
2.  **Storage:** Storing these vectors in a Vector Database (like **ChromaDB**).
3.  **Retrieval & Generation:** When a user asks a question, the system searches the VectorDB for the most relevant chunks, injects them into the prompt, and asks the LLM to generate an answer based *only* on that context.

## 3. Agentic Workflows with LangGraph

While Chains are linear and predictable, **Agents** are dynamic. 
*   **LangGraph** allows you to build stateful, multi-actor applications by defining workflows as graphs (nodes and edges).
*   Instead of a hardcoded sequence, agents can use LLMs to *decide* the next step, loop back for corrections, or execute tasks in parallel or sequence.

> **Next Step:** Proceed to `instructions.md` for a guided learning path through the notebooks in this directory, which will take you from basic API calls to building complex multi-agent systems.
