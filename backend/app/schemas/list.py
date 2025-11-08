from pydantic import BaseModel
from typing import Optional, Dict, Any


class ListRequest(BaseModel):
    query: Optional[str] = None
    filters: Optional[Dict[str, Any]] = None


class ListResponse(BaseModel):
    status: str
    items: list[Dict[str, Any]]
