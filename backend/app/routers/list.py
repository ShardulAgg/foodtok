from fastapi import APIRouter
from app.schemas.list import ListRequest, ListResponse, TrendItem
import json
from pathlib import Path

router = APIRouter(
    prefix="/api/v1/list",
    tags=["list"]
)

# JSON database path
DB_PATH = Path(__file__).parent.parent.parent / "data" / "analysis.json"


def load_db():
    """Load analysis database from JSON file"""
    if not DB_PATH.exists():
        return []
    with open(DB_PATH, "r") as f:
        return json.load(f)


@router.post("/", response_model=ListResponse)
async def list_items(request: ListRequest):
    """List all analyzed trends from database"""
    # Load trends from database
    trends_data = load_db()

    # Convert to TrendItem objects
    trends = [TrendItem(**item) for item in trends_data]

    return ListResponse(
        status="success",
        trends=trends
    )
