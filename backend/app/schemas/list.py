from pydantic import BaseModel
from typing import List


class TrendItem(BaseModel):
    trend_name: str
    video_reference: str
    why_trending: str
    category: str


class ListRequest(BaseModel):
    pass


class ListResponse(BaseModel):
    status: str
    trends: List[TrendItem]
