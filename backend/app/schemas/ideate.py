from pydantic import BaseModel
from typing import Optional, Dict, Any


class IdeateRequest(BaseModel):
    prompt: str
    context: Optional[Dict[str, Any]] = None


class IdeateResponse(BaseModel):
    status: str
    ideas: list[str]
