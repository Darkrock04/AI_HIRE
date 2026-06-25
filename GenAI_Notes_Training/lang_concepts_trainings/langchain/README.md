# LangChain Concepts & Training

Welcome to the **LangChain** module! This folder is designed to take you from a complete beginner to a master of the LangChain framework. Before diving into the `.ipynb` code files, please read this theoretical guide.

---

## 🧠 What is LangChain?
LangChain is an open-source framework designed to simplify the creation of applications using large language models (LLMs). If an LLM is the "brain", LangChain is the "nervous system" that connects that brain to the outside world (databases, internet, tools, memory).

### The Core Problem it Solves
By themselves, LLMs like GPT-4 or DeepSeek cannot:
1. Remember past conversations.
2. Read your private company PDFs.
3. Search the internet.
4. Do math or execute code.

LangChain provides the "glue" to make all of this happen in just a few lines of Python.

---

## 🏗️ The 6 Pillars of LangChain

### 1. Models & Prompts
*   **Models:** LangChain provides a universal interface. Instead of writing custom code for OpenAI, then rewriting it for Anthropic, then rewriting it for Groq... LangChain lets you swap out models with one line of code.
*   **Prompt Templates:** Instead of hardcoding strings, you use templates with `{variables}` to dynamically inject user input into expert instructions.

### 2. Output Parsers
LLMs output raw text (strings). But as a developer, you usually need structured data (like a Python Dictionary or JSON). **Output Parsers** force the LLM to reply in a specific format and automatically convert that text into usable code objects.

### 3. Chains (LCEL)
**LangChain Expression Language (LCEL)** uses the pipe operator `|` to chain components together.
A classic chain looks like this:
`chain = prompt | model | output_parser`
Data flows from left to right seamlessly.

### 4. Memory
By default, LLMs have amnesia. They don't remember the previous question you asked. LangChain provides **Memory** components (like `ConversationBufferMemory`) that automatically store conversation history and inject it into the prompt so the AI can "remember".

### 5. RAG (Retrieval-Augmented Generation)
How do you let an AI read a 500-page PDF? You can't just paste it into the prompt.
1.  **Document Loaders:** Extract text from PDFs, URLs, or databases.
2.  **Text Splitters:** Chop the massive text into smaller "chunks".
3.  **Embeddings:** Convert those text chunks into numbers (vectors).
4.  **Vector Stores (ChromaDB):** A specialized database to store these number-chunks.
5.  **Retrievers:** When a user asks a question, the retriever searches the Vector Store for the most relevant chunks and gives *only* those chunks to the LLM to answer the question.

### 6. Agents
Chains are hardcoded sequences (Step A -> Step B -> Step C).
**Agents** are dynamic. You give an Agent an objective and a box of Tools (like a Calculator, a Google Search tool, and a SQL query tool). The Agent uses its "brain" to decide *which* tools to use, and in *what order*, to solve the problem.

---

## 🚀 How to Practice
Now that you understand the theory, open the `.ipynb` files in this directory in numerical order. 

1. Start with `01_intro_to_langchain.ipynb` to see basic prompts.
2. Work your way up to `05` and `06` to build a complete RAG application!
