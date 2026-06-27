# Middleware & Callbacks
In AI applications, middleware allows you to intercept the process *before* hitting the LLM (caching, summarization) and *after* the LLM generates a response (streaming, token tracking).

This module covers:
1. Custom Callbacks for Streaming.
2. Caching to save API costs.
3. Chat Summarization to prevent hitting token limits.