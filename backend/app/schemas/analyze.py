from pydantic import BaseModel
from typing import Optional, Dict, Any


class AnalyzeRequest(BaseModel):
    content: str
    options: Optional[Dict[str, Any]] = None


class AnalyzeResponse(BaseModel):
    status: str
    result: Dict[str, Any]
