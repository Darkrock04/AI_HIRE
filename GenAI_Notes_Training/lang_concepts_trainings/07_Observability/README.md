# Observability

## 1. Tracing with Langfuse
When you build complex Agents or RAG pipelines, you lose visibility into what the LLM is actually doing.
# Observability

## 1. Tracing with Langfuse
When you build complex Agents or RAG pipelines, you lose visibility into what the LLM is actually doing.
**Langfuse** is an open-source observability platform that tracks every single step of your chain.
By passing the Langfuse `CallbackHandler` into your chain execution, you get a beautiful UI that shows:
- The exact prompt sent to the LLM (after all templates are injected)
- The exact raw output
- How many tokens were used and the total cost (e.g., $0.002)
- How many milliseconds the request took
- Which tools the agent decided to use and what the internet search returned

## Streaming
Users hate waiting 20 seconds for a large response. Streaming allows the LLM to yield tokens one by one to the frontend in real-time, drastically improving perceived latency.
