from pydantic import BaseModel, Field
from datetime import datetime


class CuttingPartRequest(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=200,
    )

    width: float = Field(
        gt=0,
    )

    height: float = Field(
        gt=0,
    )

    quantity: int = Field(
        gt=0,
    )


class CuttingRequest(BaseModel):
    material_id: int = Field(gt=0)

    sheet_width: float = Field(gt=0)
    sheet_height: float = Field(gt=0)

    parts: list[CuttingPartRequest] = Field(
        min_length=1,
    )


class PlacementResponse(BaseModel):
    part_name: str

    x: float
    y: float

    width: float
    height: float

    rotated: bool


class CuttingResponse(BaseModel):
    sheet_width: float
    sheet_height: float

    sheet_area: float
    placed_area: float
    waste_area: float
    utilization: float

    placements: list[PlacementResponse]
    unplaced_parts: list[CuttingPartRequest]


class CuttingPlanResponse(BaseModel):
    id: int
    material_id: int

    used_area: float
    waste_area: float
    utilization: float

    created_at: datetime

    model_config = {
        "from_attributes": True,
    }