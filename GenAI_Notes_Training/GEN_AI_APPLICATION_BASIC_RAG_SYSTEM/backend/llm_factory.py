import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel

load_dotenv(override=True)

def get_llm() -> BaseChatModel:
    """
    Returns a single LLM instance for the entire RAG system.

    HOW TO SWITCH MODELS:
    - Change ACTIVE_PROVIDER in .env to 'nvidia' or 'self_hosted'
    - Change the model name below to use a different model
    """

    # -----------------------------------------------------------------
    # MODEL NAMES (Change these strings to swap models)
    # -----------------------------------------------------------------
    NVIDIA_MODEL = "nvidia/nemotron-3-super-120b-a12b"        # <-- Change this for NVIDIA
    SELF_HOSTED_MODEL = "qwen2.5:14b"                    # <-- Change this for Self-Hosted

    active_provider = os.getenv("ACTIVE_CHAT_PROVIDER", "nvidia")

    if active_provider == "nvidia":
        return ChatOpenAI(
            api_key=os.getenv("NVIDIA_API_KEY"),
            base_url="https://integrate.api.nvidia.com/v1",
            model=NVIDIA_MODEL,
            max_tokens=2048,
        )
    else:
        return ChatOpenAI(
            api_key=os.getenv("SELF_HOSTED_API_KEY", "self_hosted"),
            base_url=os.getenv("SELF_HOSTED_API_BASE", "https://rock0230-local.hf.space/v1"),
            model=SELF_HOSTED_MODEL,
            max_tokens=2048,
        )
