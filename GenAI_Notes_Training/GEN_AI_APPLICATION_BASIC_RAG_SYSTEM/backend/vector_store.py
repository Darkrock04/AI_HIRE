import os
import logging
from dotenv import load_dotenv

load_dotenv(override=True)

# Disable ChromaDB telemetry to keep logs clean
os.environ["ANONYMIZED_TELEMETRY"] = "False"

from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DB_DIR = os.path.join(os.path.dirname(__file__), "..", "chroma_db")

# Supported file types
SUPPORTED_EXTENSIONS = {".pdf", ".txt"}
MAX_FILE_SIZE_BYTES = 20 * 1024 * 1024  # 20MB

# -----------------------------------------------------------------
# EMBEDDING MODEL NAMES (Change these to swap embedding models)
# -----------------------------------------------------------------
NVIDIA_EMBED_MODEL = "nvidia/nv-embedqa-e5-v5"          # <-- Change this for public_model
SELF_HOSTED_EMBED_MODEL = "nomic-embed-text:latest"       # <-- Change this for Self-Hosted


def _get_embedding_function():
    """
    Returns the correct embedding function based on ACTIVE_EMBED_PROVIDER in .env.
    """
    active_provider = os.getenv("ACTIVE_EMBED_PROVIDER", "nvidia")

    if active_provider == "nvidia":
        logger.info(f"Using NVIDIA embeddings: {NVIDIA_EMBED_MODEL}")
        return OpenAIEmbeddings(
            api_key=os.getenv("NVIDIA_API_KEY"),
            base_url="https://integrate.api.nvidia.com/v1",
            model=NVIDIA_EMBED_MODEL,
            check_embedding_ctx_length=False,
            chunk_size=1,
            # NVIDIA asymmetric models need input_type in the request body.
            # extra_body injects it directly into the HTTP JSON payload.
            model_kwargs={"extra_body": {"input_type": "passage"}}
        )
    else:
        base_url = os.getenv("SELF_HOSTED_API_BASE", "https://rock0230-local.hf.space/v1").rstrip("/v1")
        logger.info(f"Using Self-Hosted embeddings: {SELF_HOSTED_EMBED_MODEL} @ {base_url}")
        return OllamaEmbeddings(
            model=SELF_HOSTED_EMBED_MODEL,
            base_url=base_url,
        )


class VectorStoreManager:
    def __init__(self):
        """Connect to the embedding model and initialize ChromaDB."""
        try:
            self.embedding_function = _get_embedding_function()
            self.db = Chroma(
                persist_directory=DB_DIR,
                embedding_function=self.embedding_function,
                collection_name="rag_session"
            )
            logger.info("VectorStoreManager initialized successfully.")
        except Exception as e:
            logger.error(f"CRITICAL: Failed to initialize VectorStoreManager: {e}")
            raise RuntimeError(f"Could not connect to embedding server: {e}")

    def ingest_document(self, file_path: str) -> int:
        """
        Load a document, split it into chunks, embed it, and store in ChromaDB.
        Returns the number of chunks added.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        if os.path.getsize(file_path) == 0:
            raise ValueError("The uploaded file is empty.")

        # --- Load ---
        ext = os.path.splitext(file_path)[1].lower()
        try:
            if ext == ".pdf":
                loader = PyPDFLoader(file_path)
            else:
                try:
                    loader = TextLoader(file_path, encoding="utf-8")
                except Exception:
                    loader = TextLoader(file_path, encoding="latin-1")
            raw_documents = loader.load()
        except Exception as e:
            raise ValueError(f"Could not read '{os.path.basename(file_path)}': {e}")

        if not raw_documents or all(not doc.page_content.strip() for doc in raw_documents):
            raise ValueError("No readable text found. It may be a scanned image PDF.")

        # --- Chunk ---
        splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=128)
        docs = splitter.split_documents(raw_documents)

        if not docs:
            raise ValueError("Chunking produced zero chunks.")

        # --- Add metadata ---
        source_name = os.path.basename(file_path)
        for i, doc in enumerate(docs):
            doc.metadata["chunk_index"] = i
            doc.metadata["source_file"] = source_name

        # --- Duplicate check and store ---
        try:
            existing = self.db.get(where={"source_file": source_name})
            if existing and existing.get("ids"):
                logger.warning(f"'{source_name}' already ingested. Skipping duplicate.")
                return len(existing["ids"])

            self.db.add_documents(docs)
            logger.info(f"Ingested '{source_name}' ({len(docs)} chunks).")
            return len(docs)
        except Exception as e:
            raise RuntimeError(f"Failed to save to ChromaDB: {e}")

    def retrieve_context(self, query: str, k: int = 4) -> str:
        """Retrieve the top-k most relevant chunks for a query."""
        try:
            results = self.db.similarity_search(query, k=k)
            if not results:
                return ""
            return "\n\n---\n\n".join([doc.page_content for doc in results])
        except Exception as e:
            logger.warning(f"Retrieval failed (continuing without context): {e}")
            return ""

    def clear_session(self):
        """
        Windows-safe session cleanup.
        Instead of deleting the SQLite file (which Windows locks), we clear
        all documents and switch to a fresh collection.
        """
        import uuid

        # Clear current collection data
        try:
            all_ids = self.db.get()["ids"]
            if all_ids:
                self.db.delete(ids=all_ids)
            logger.info(f"Cleared {len(all_ids)} chunks from collection.")
        except Exception as e:
            logger.warning(f"Could not clear collection: {e}")

        # Switch to a new empty collection
        new_name = f"session_{uuid.uuid4().hex[:8]}"
        self.db = Chroma(
            persist_directory=DB_DIR,
            embedding_function=self.embedding_function,
            collection_name=new_name
        )
        logger.info(f"New session: '{new_name}'")


vector_store_manager = VectorStoreManager()
