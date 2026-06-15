from pydantic import BaseModel
from typing import Optional, List

class ChatMessage(BaseModel):
    """A single message in the conversation."""
    role: str      # 'user' or 'assistant'
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[ChatMessage]] = []

class ChatResponse(BaseModel):
    response: str
    status: str

class DocumentUploadResponse(BaseModel):
    message: str
    chunks_added: int
