# LangGraph

Standard LangChain Agents (like ReAct) are powerful but notoriously unreliable for complex, multi-step tasks. Because the LLM is completely in control of the loop, it often gets confused, loops infinitely, or uses the wrong tools.

**LangGraph** solves this by letting developers explicitly define the workflow as a State Graph (Nodes and Edges).

## Key Concepts
1. **State:** A python dictionary (or Pydantic model) that holds the current state of the application. It gets passed from node to node.
2. **Nodes:** Python functions that execute logic (e.g., calling an LLM, querying a database) and update the State.
3. **Edges:** The arrows connecting the nodes. They dictate the flow.
4. **Conditional Edges:** Dynamic arrows that use an LLM's decision to route the graph (e.g., If the document is irrelevant, loop back to the Search node. If relevant, proceed to the Generate node).
