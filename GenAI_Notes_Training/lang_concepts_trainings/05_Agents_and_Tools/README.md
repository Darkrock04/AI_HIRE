# Agents and Tools

A Chain is deterministic: the sequence of steps is hardcoded by the developer (e.g., prompt -> llm -> parser).
An **Agent** is non-deterministic: the LLM itself decides which steps to take and which tools to use.

## Tools & Knowledge Cutoffs
LLMs are frozen in time (e.g., they only know data up to 2023). If you ask for the weather today, they hallucinate. 
We solve this by giving them **Tools**. A common tool is the `DuckDuckGoSearchRun` tool, which allows the LLM to pause its generation, search the live internet, read the results, and *then* answer the user perfectly.

## Agent Types
- **Agent With Tool:** A modern tool-calling agent uses specialized models (like LLaMA 3 or GPT-4o) that are fine-tuned to know *when* and *how* to use a tool. You bind the tools to the LLM and let it act autonomously.
- **Agent With Middleware:** As agents think and browse the web, they consume massive amounts of tokens. **Middleware** (like `SummarizationMiddleware`) acts as an interceptor. It silently tracks the agent's memory size in the background. If the token count hits a dangerous limit (e.g., 4000 tokens), the Middleware intercepts the memory, uses a smaller LLM to summarize the old messages, and gives the fresh, compressed memory back to the main Agent, preventing crashes.
