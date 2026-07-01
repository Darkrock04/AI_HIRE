# Observability

When you deploy a complex LangGraph or LCEL chain to production, you need to know exactly what is happening under the hood. Which tool took 10 seconds to execute? How many tokens did the LLM consume? 

## LangSmith & Langfuse
These are tracing platforms. By simply injecting a callback handler into your chain, they log every single step of execution (prompts, responses, latency, cost) into a beautiful visual dashboard.

## Streaming
Users hate waiting 20 seconds for a large response. Streaming allows the LLM to yield tokens one by one to the frontend in real-time, drastically improving perceived latency.
