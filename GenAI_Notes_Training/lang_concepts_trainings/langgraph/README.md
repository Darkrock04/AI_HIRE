# LangGraph Concepts & Training

Welcome to the **LangGraph** module! While LangChain is great for simple, linear workflows, modern AI applications require complex, cyclical, multi-agent systems. That is exactly what LangGraph solves.

Before diving into the code, read this guide to understand the fundamental shift from Chains to Graphs.

---

## 🕸️ What is LangGraph?
LangGraph is an extension of LangChain designed specifically for building robust, stateful, multi-actor applications with LLMs. It brings the mathematical concept of **Graph Theory** to AI.

If a standard LangChain application is a "conveyor belt" (data goes in one direction), a LangGraph application is a "flowchart" (data can loop, branch, and make complex decisions).

---

## 🧱 The Core Concepts of LangGraph

### 1. State (The Memory)
In LangGraph, the most important concept is the **State**. 
Think of the State as a global dictionary (or `TypedDict` in Python) that gets passed from step to step. Every time a step completes, it updates this global State. This allows the graph to "remember" exactly what is happening at any given moment.

### 2. Nodes (The Workers)
A Node is simply a Python function. It takes the current State as input, does some work (like calling an LLM, searching the web, or parsing data), and then returns an update to the State.
*   **Agent Node:** An LLM deciding what to do.
*   **Tool Node:** A python script doing math or searching Google.

### 3. Edges (The Connections)
Edges connect the Nodes together. They dictate the flow of the application.
*   **Standard Edges:** "After Node A is done, *always* go to Node B."
*   **Conditional Edges:** "After Node A is done, run a Python function to decide whether we should go to Node B, or loop back to Node C."

### 4. Cycles (Loops)
This is LangGraph's superpower. Traditional LangChain pipelines cannot loop (e.g., "Keep asking the user questions until we have all the required information"). Because LangGraph is a graph, you can easily draw an Edge from the end of the process back to the beginning, creating intelligent, autonomous loops.

### 5. Checkpointing (Time Travel)
LangGraph allows you to save the State at every single step to a database (like SQLite). This allows you to:
*   Pause an execution and wait for human approval (Human-in-the-loop).
*   "Rewind" the AI to a previous step if it makes a mistake.
*   Resume long-running tasks exactly where they left off.

---

## 🚦 Types of Workflows

As you go through the notebooks, you will build:
1.  **Sequential Workflows:** Simple linear step-by-step processes.
2.  **Parallel Workflows:** Running multiple nodes at the exact same time to save time.
3.  **Conditional Workflows:** Making intelligent "If/Else" decisions based on AI outputs.

---

## 🚀 How to Practice
Open the `.ipynb` files in this directory in numerical order. You will start with a basic graph and slowly build up to complex, multi-agent routing systems!
