# LangGraph

Standard LangChain Agents (like ReAct) are powerful but notoriously unreliable for complex, multi-step tasks. Because the LLM is completely in control of the loop, it often gets confused, loops infinitely, or uses the wrong tools.

**LangGraph is a framework for building stateful, multi-actor applications with LLMs. Unlike simple LCEL chains that run straight through from start to finish (like a pipeline), LangGraph allows you to build **cycles**, meaning the agent can loop back and try again if it makes a mistake.

## Core Concepts
LangGraph models your application as a State Machine.
1. **State:** A shared data structure (usually a `TypedDict`) that is passed around. Every time a node runs, it returns updates that are merged into this state.
2. **Nodes:** Simple Python functions. A node receives the current `State`, does some work (like calling an LLM or a tool), and returns a dictionary to update the `State`.
3. **Edges:** Hardcoded paths connecting one node to the next (e.g., Node A *always* goes to Node B).
4. **Conditional Edges:** Dynamic routing functions. The function looks at the current `State` and decides where to go next (e.g., if there's an error, route to the "Fixer" node, otherwise route to `END`).
