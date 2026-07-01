# Chains and LangChain Expression Language (LCEL)

In the old days of LangChain, you had to use legacy classes like `LLMChain` or `ConversationalRetrievalChain`. Today, the standard is **LCEL** (LangChain Expression Language).

## LCEL Syntax (`|`)
LCEL uses the Linux pipe operator `|` to pass the output of one component directly into the input of the next. It makes code infinitely cleaner and automatically supports streaming, batching, and async operations out of the box.

`chain = prompt | llm | output_parser`

## Advanced LCEL
- **Routing:** You can build chains that dynamically choose which sub-chain to run based on the user's input (e.g., routing math questions to a Math prompt, and coding questions to a Code prompt).
- **Fallbacks:** You can attach fallback models so if the primary LLM API goes down, the chain seamlessly switches to a backup model without crashing.
