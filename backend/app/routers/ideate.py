from fastapi import APIRouter
from app.schemas.ideate import IdeateRequest, IdeateResponse

router = APIRouter(
    prefix="/api/v1/ideate",
    tags=["ideate"]
)

@router.post("/", response_model=IdeateResponse)
async def ideate(request: IdeateRequest):
    """Generate ideas based on prompt"""
    # Add your ideation logic here
    ideas = []

    return IdeateResponse(
        status="success",
        ideas=ideas
    )
