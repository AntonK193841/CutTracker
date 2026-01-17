from datetime import datetime

from pydantic import BaseModel, Field


class MaterialCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    grade: str = Field(min_length=1, max_length=100)

    thickness: float = Field(gt=0)
    width: float = Field(gt=0)
    height: float = Field(gt=0)

    quantity: int = Field(ge=0)


class MaterialResponse(BaseModel):
    id: int
    name: str
    grade: str

    thickness: float
    width: float
    height: float

    quantity: int
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }