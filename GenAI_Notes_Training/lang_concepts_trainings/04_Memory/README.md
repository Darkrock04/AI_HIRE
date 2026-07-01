# Memory

LLMs are fundamentally stateless. Every API call is independent. If you want a chatbot to remember what you said 5 minutes ago, you must explicitly pass the entire conversation history into the prompt every single time.

LangChain provides specialized tools to manage this history automatically.

## How LCEL Handles Memory
In the modern LangChain Expression Language (LCEL), we explicitly pass memory into the prompt.
1. **`InMemoryChatMessageHistory`**: An object that stores all the Human and AI messages in a list.
2. **`MessagesPlaceholder`**: A special variable inside your `ChatPromptTemplate` that tells the prompt exactly where to inject the conversational history list before asking the newest question.
