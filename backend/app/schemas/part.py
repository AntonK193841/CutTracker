from datetime import datetime

from pydantic import BaseModel, Field


class PartCreate(BaseModel):
    drawing_number: str = Field(
        min_length=1,
        max_length=100,
    )

    name: str = Field(
        min_length=1,
        max_length=200,
    )

    width: float = Field(gt=0)
    height: float = Field(gt=0)

    quantity: int = Field(
        gt=0,
    )

    material_id: int = Field(
        gt=0,
    )


class PartResponse(BaseModel):
    id: int
    drawing_number: str
    name: str

    width: float
    height: float
    quantity: int

    material_id: int
    created_at: datetime

    model_config = {
        "from_attributes": True,
    }