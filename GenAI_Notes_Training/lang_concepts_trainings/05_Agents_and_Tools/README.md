# Agents and Tools

A Chain is deterministic: the sequence of steps is hardcoded by the developer (e.g., prompt -> llm -> parser).
An **Agent** is non-deterministic: the LLM itself decides which steps to take and which tools to use.

## Tools
A tool is simply a Python function (like calling an API, checking a database, or doing math) that the LLM is allowed to trigger.

## ReAct Agents
ReAct stands for **Reasoning and Acting**. It is the most common agent framework where the LLM is given a prompt forcing it to output a `Thought` (what it should do), an `Action` (the tool to use), and an `Action Input` (the parameters for the tool). The agent executes the tool, returns the `Observation` to the LLM, and repeats until it has the final answer.
