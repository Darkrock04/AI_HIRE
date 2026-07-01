# Model I/O

The core of any LLM application is communicating with the model. LangChain provides a standardized interface (Model I/O) to manage this communication regardless of which underlying model provider (OpenAI, Anthropic, Groq, HuggingFace) you use.

## 1. LLMs and Chat Models
- **LLMs:** Older models that take a single string as input and return a string (e.g., `text-davinci-003`).
- **Chat Models:** Modern models (like GPT-4 or LLaMA 3) that take a list of structured messages (System, Human, AI) as input. This is the industry standard.

## 2. Prompt Templates
Hardcoding strings is bad practice. **Prompt Templates** allow you to create dynamic, reusable recipes for your prompts.
- `PromptTemplate`: Used for older string-based LLMs.
- `ChatPromptTemplate`: Used for modern Chat Models. It allows you to strictly separate System instructions from Human input.

## 3. Output Parsers
LLMs output raw text. If you are building an application, you usually need structured data (like JSON or a Python Dictionary). **Output Parsers** force the LLM to reply in a specific format and automatically parse that text into a usable Python object.
