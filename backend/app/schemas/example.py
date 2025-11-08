from pydantic import BaseModel
from typing import Optional


class ExampleBase(BaseModel):
    """Base example schema"""
    name: str
    description: Optional[str] = None


class ExampleCreate(ExampleBase):
    """Schema for creating an example"""
    pass


class ExampleResponse(ExampleBase):
    """Schema for example response"""
    id: int

    class Config:
        from_attributes = True
