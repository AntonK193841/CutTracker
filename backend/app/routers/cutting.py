from fastapi import APIRouter

from app.domain.nesting import NestingCalculator
from app.domain.part import Part
from app.domain.sheet import Sheet
from app.schemas.cutting import (
    CuttingRequest,
    CuttingResponse,
    PlacementResponse,
)


router = APIRouter(
    prefix="/api/cutting",
    tags=["Cutting"],
)


@router.post(
    "/calculate",
    response_model=CuttingResponse,
)
def calculate_cutting(
    data: CuttingRequest,
):
    sheet = Sheet(
        width=data.sheet_width,
        height=data.sheet_height,
    )

    parts = [
        Part(
            name=part.name,
            width=part.width,
            height=part.height,
            quantity=part.quantity,
        )
        for part in data.parts
    ]

    calculator = NestingCalculator()

    result = calculator.calculate(
        sheet=sheet,
        parts=parts,
    )

    placements = [
        PlacementResponse(
            part_name=placement.part.name,
            x=placement.x,
            y=placement.y,
            width=placement.width,
            height=placement.height,
            rotated=placement.rotated,
        )
        for placement in result.placements
    ]

    return CuttingResponse(
        sheet_width=sheet.width,
        sheet_height=sheet.height,
        sheet_area=sheet.area,
        placed_area=result.placed_area,
        waste_area=result.waste_area,
        utilization=result.utilization,
        placements=placements,
        unplaced_parts=[
            {
                "name": part.name,
                "width": part.width,
                "height": part.height,
                "quantity": part.quantity,
            }
            for part in result.unplaced_parts
        ],
    )