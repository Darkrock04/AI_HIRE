# Memory

LLMs are fundamentally stateless. Every API call is independent. If you want a chatbot to remember what you said 5 minutes ago, you must explicitly pass the entire conversation history into the prompt every single time.

LangChain provides specialized tools to manage this history automatically.

## Memory Types:
1. **ConversationBufferMemory:** Stores every raw message exactly as it happened. Good for short chats, but rapidly consumes the LLM's token limit.
2. **ConversationSummaryMemory:** Uses a smaller, cheaper LLM in the background to constantly summarize the conversation history, saving massive amounts of tokens.
