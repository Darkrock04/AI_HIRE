# Model I/O

The core of any LLM application is communicating with the model. LangChain provides a standardized interface (Model I/O) to manage this communication regardless of which underlying model provider (OpenAI, Anthropic, Groq, HuggingFace) you use.

## 1. LLMs and Chat Models
- **LLMs:** Older models that take a single string as input and return a string (e.g., `text-davinci-003`).
- **Chat Models:** Modern models (like GPT-4 or LLaMA 3) that take a list of structured messages (System, Human, AI) as input. This is the industry standard.

## 2. Prompt Templates
Hardcoding strings is bad practice. **Prompt Templates** allow you to create dynamic, reusable recipes for your prompts. 

There are several ways to construct templates depending on your needs:

### A. `ChatPromptTemplate.from_template()`
Use this when you just have a **single string** that you want to inject variables into. Behind the scenes, LangChain automatically converts this single string into a `HumanMessage`. 
- **Best for:** Simple, quick questions where you don't need complex System instructions.
- **Example:** `ChatPromptTemplate.from_template("Translate {word} to French.")`

### B. `ChatPromptTemplate.from_messages()`
Use this when you want **strict control** over the roles in the conversation (System, Human, AI). Modern models perform much better when instructions are explicitly categorized.
- **Best for:** Complex agents, maintaining chat history, and setting strict behavioral instructions.
- **Example:** 
  ```python
  ChatPromptTemplate.from_messages([
      ("system", "You are a helpful translation assistant."),
      ("human", "Translate {word} to French.")
  ])
  ```

### C. Advanced Templates
- **`FewShotPromptTemplate`:** Used when you want to pass multiple examples (Input -> Output) to the model before asking your actual question. This drastically improves the model's accuracy on formatting tasks.
- **`PromptTemplate`:** The legacy class used for older, non-chat LLMs (models that just take a single string, rather than messages). Rarely used in modern applications.

## 3. Output Parsers
LLMs output raw text. When building an application, you often want to extract just the final text without all the metadata, or force the LLM to reply in a specific format. **Output Parsers** (like `StrOutputParser`) take the raw LLM message object and parse it into a clean, usable format (like a plain string).
