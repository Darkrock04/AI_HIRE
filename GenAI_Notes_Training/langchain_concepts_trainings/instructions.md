# The GenAI Learning Workflow: A Step-by-Step Guide

Welcome! This guide outlines the recommended progression through the Jupyter Notebooks in this folder to build your expertise from basic LLM interactions to advanced Agentic workflows.

## Step 1: Basics & API Providers
Start by understanding how to connect to fast, cloud-based LLMs.
*   👉 **Notebook:** `langchain_groq_intro.ipynb`
*   **Goal:** Learn how to set up an LLM client, pass system and human messages, and generate basic completions.

## Step 2: Chains and Memory
LLMs are stateless by default. We need to chain operations and add memory to build conversational bots.
*   👉 **Notebooks:** `langchain_chain_app.ipynb` & `langchain_memory_app.ipynb`
*   **Goal:** Learn how to create `PromptTemplates`, link them with LLMs using `LCEL` (LangChain Expression Language), and implement buffer memory so the AI remembers context.

## Step 3: Retrieval-Augmented Generation (RAG)
Teach the AI to answer questions based on your custom documents (like PDFs).
*   👉 **Notebooks:** `langchain_pdf_chromadb_part1.ipynb` & `langchain_pdf_chromadb_part2.ipynb`
*   **Goal:** Master the RAG pipeline. You will learn to load PDFs, split them into chunks, create embeddings, store them in ChromaDB, and build a retriever to fetch context for the LLM.

## Step 4: Advanced Agentic Workflows (LangGraph)
Move beyond linear chains and build intelligent agents that can reason, plan, and loop.
*   👉 **Notebooks:** `intro_to_langgraph.ipynb`, `seq_graph_workflows.ipynb`, and `parallel_graph_workflows.ipynb`
*   **Goal:** Understand how to define `State`, create Nodes (functions), and define Edges (conditional routing). You'll learn the difference between sequential execution and running agents in parallel.

## Step 5: Observability and LLMOps
Once your application is built, you need to monitor it.
*   👉 **Notebook:** `observability_llmops.ipynb`
*   **Goal:** Learn how to use tools like LangSmith to trace LLM calls, monitor token usage, debug prompts, and ensure your system is running reliably in production.

---
> 💡 **Tip:** After mastering these notebooks, you will be ready to understand and modify the complete production-grade application located in the `GEN_AI_APPLICATION_BASIC_RAG_SYSTEM` folder!
