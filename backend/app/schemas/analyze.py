from pydantic import BaseModel
from typing import Optional


class AnalyzeRequest(BaseModel):
    video_path: str


class AnalyzeResponse(BaseModel):
    status: str
    message: str
