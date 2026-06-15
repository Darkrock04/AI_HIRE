import logging
from langchain_core.prompts import ChatPromptTemplate
from backend.llm_factory import get_llm
from backend.vector_store import vector_store_manager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =========================================================================
# SINGLE LLM — One model does everything
# =========================================================================
try:
    llm = get_llm()
    logger.info("LLM initialized successfully.")
except Exception as e:
    logger.critical(f"FATAL: Could not initialize LLM. Check .env config. Error: {e}")
    raise

# =========================================================================
# SYSTEM PROMPT — Defines the AI's behavior
# =========================================================================
SYSTEM_PROMPT = """You are a helpful AI Assistant that answers questions based on uploaded documents and general knowledge.

IDENTITY RULES:
- You are the "AI Assistant" — never reveal the underlying model name.
- If asked who you are, say: "I am the AI Assistant."

ANSWERING RULES:
- If document context is provided and relevant, use it to answer accurately.
- If no document context is provided, answer from your general knowledge.
- Be concise and direct. No unnecessary filler.
- For greetings like 'hello' or 'hi', respond briefly and naturally.

Conversation History:
{history}

Document Context (from uploaded files):
{context}

User Question: {question}

Answer:"""


def process_chat(message: str, history: list = None) -> str:
    """
    Basic RAG pipeline:
    1. Retrieve relevant chunks from ChromaDB
    2. Format prompt with context + history
    3. Send to LLM and return the answer

    That's it. No planners, no routers, no validators, no feedback loops.
    """

    # --- Format conversation history ---
    history_str = "No previous conversation."
    if history:
        lines = []
        for msg in history[-6:]:  # Last 3 turns
            role = "User" if msg.get("role") == "user" else "Assistant"
            lines.append(f"{role}: {msg.get('content', '')}")
        if lines:
            history_str = "\n".join(lines)

    # --- Retrieve context from ChromaDB ---
    context = vector_store_manager.retrieve_context(message)
    if not context:
        context = "No documents uploaded yet."

    # --- Generate answer ---
    try:
        prompt = ChatPromptTemplate.from_template(SYSTEM_PROMPT)
        result = (prompt | llm).invoke({
            "history": history_str,
            "context": context,
            "question": message
        })
        answer = result.content if hasattr(result, "content") else str(result)
        return answer.strip() if answer and answer.strip() else "I couldn't generate a response. Please try again."
    except Exception as e:
        logger.error(f"LLM call failed: {e}")
        return f"Sorry, an error occurred: {str(e)[:200]}"
