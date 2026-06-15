# Generative AI (GenAI) 💬

**What is Generative AI?**
While traditional ML predicts a number (like price) or a category (like spam), Generative AI actually creates *new* content. Large Language Models (LLMs) like ChatGPT, DeepSeek, or Qwen can write essays, write code, or hold human-like conversations.

## How Does Training Work Here?
**Plot twist: We usually don't train them from scratch!** 
Training a massive LLM requires millions of dollars and supercomputers. Instead, "training" or building apps in GenAI usually means **prompting and connecting**:
1. **API Calls:** We connect to a massive, already-trained AI model hosted in the cloud.
2. **Context Injection (RAG):** If we want the AI to know about our private company documents, we don't retrain it. Instead, we search our documents, find the relevant paragraphs, and paste them into the Prompt alongside the user's question.
3. **Agentic Workflows:** We write code that gives the AI "tools" (like the ability to search the web or run a calculator) and let it autonomously decide how to solve complex problems step-by-step.

## Python Modules Used for GenAI
Building GenAI applications requires a completely different toolset than ML or DL:

*   **`langchain`:** The ultimate framework for GenAI. It helps us easily connect to LLMs, format Prompts, and give the AI "Memory" so it remembers past conversations.
*   **`langgraph`:** A tool for building autonomous AI "Agents" that can loop, think, and make decisions dynamically.
*   **`chromadb`:** A specialized "Vector Database". It is used in RAG to store our private documents as mathematical numbers so we can instantly search them for relevant context.
*   **API Providers (`groq`):** The libraries used to securely talk to the giant cloud models over the internet.
