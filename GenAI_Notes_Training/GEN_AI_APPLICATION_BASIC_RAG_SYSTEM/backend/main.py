import os
import logging
from fastapi import FastAPI, UploadFile, File
from backend.api_models import ChatRequest, ChatResponse, DocumentUploadResponse
from backend.graph_agent import process_chat
from backend.vector_store import vector_store_manager, SUPPORTED_EXTENSIONS, MAX_FILE_SIZE_BYTES

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Basic RAG API", version="1.0")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """Send a message → Retrieve context → LLM answers."""
    if not request.message or not request.message.strip():
        return ChatResponse(response="Please type a message.", status="error")

    user_message = request.message.strip()[:5000]  # Cap at 5000 chars
    history_dicts = [{"role": m.role, "content": m.content} for m in (request.history or [])]

    try:
        answer = process_chat(user_message, history=history_dicts)
        if not answer or not answer.strip():
            answer = "I couldn't generate a response. Please try rephrasing."
        return ChatResponse(response=answer, status="success")
    except Exception as e:
        logger.error(f"Chat error: {e}")
        return ChatResponse(response=f"Error: {str(e)[:200]}", status="error")


@app.post("/upload_doc", response_model=DocumentUploadResponse)
async def upload_document(file: UploadFile = File(...)):
    """Upload a PDF or TXT → Chunk → Embed → Store in ChromaDB."""
    filename = file.filename or "unknown"
    file_ext = os.path.splitext(filename)[1].lower()

    if file_ext not in SUPPORTED_EXTENSIONS:
        return DocumentUploadResponse(
            message=f"Unsupported type '{file_ext}'. Use: {', '.join(SUPPORTED_EXTENSIONS)}",
            chunks_added=0
        )

    safe_filename = os.path.basename(filename).replace(" ", "_")
    file_content = await file.read()

    if len(file_content) == 0:
        return DocumentUploadResponse(message="File is empty.", chunks_added=0)

    if len(file_content) > MAX_FILE_SIZE_BYTES:
        return DocumentUploadResponse(message="File too large (max 20MB).", chunks_added=0)

    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    file_path = os.path.join(data_dir, safe_filename)

    try:
        os.makedirs(data_dir, exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(file_content)

        chunks = vector_store_manager.ingest_document(file_path)
        return DocumentUploadResponse(message=f"Ingested '{safe_filename}'", chunks_added=chunks)
    except (ValueError, FileNotFoundError) as e:
        return DocumentUploadResponse(message=f"Error: {str(e)}", chunks_added=0)
    except Exception as e:
        logger.error(f"Upload error: {e}")
        return DocumentUploadResponse(message=f"System error: {str(e)[:200]}", chunks_added=0)


@app.post("/clear_session")
async def clear_session():
    """Wipe all uploaded docs and vectors for a fresh start."""
    errors = []

    try:
        vector_store_manager.clear_session()
    except Exception as e:
        errors.append(str(e))

    try:
        data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
        if os.path.exists(data_dir):
            for f in os.listdir(data_dir):
                try:
                    os.remove(os.path.join(data_dir, f))
                except Exception:
                    pass
    except Exception as e:
        errors.append(str(e))

    if errors:
        return {"status": "partial", "message": f"Errors: {'; '.join(errors)}"}
    return {"status": "success", "message": "Session cleared."}
