from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/example",
    tags=["example"]
)

@router.get("/")
async def get_examples():
    """Get all examples"""
    return {"examples": ["example1", "example2"]}

@router.get("/{item_id}")
async def get_example(item_id: int):
    """Get specific example by ID"""
    return {"item_id": item_id, "name": f"Example {item_id}"}
