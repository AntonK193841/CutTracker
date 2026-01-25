from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.domain.nesting import NestingCalculator
from app.domain.part import Part
from app.domain.sheet import Sheet
from app.repositories.cutting_plan import CuttingPlanRepository
from app.repositories.material import MaterialRepository
from app.schemas.cutting import (
    CuttingPartRequest,
    CuttingPlanResponse,
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
    db: Session = Depends(get_db),
):
    material_repository = MaterialRepository(db)

    material = material_repository.get_by_id(
        data.material_id
    )

    if material is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material not found",
        )

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

    cutting_plan_repository = CuttingPlanRepository(db)

    cutting_plan_repository.create(
        material_id=data.material_id,
        used_area=result.placed_area,
        waste_area=result.waste_area,
        utilization=result.utilization,
    )

    return CuttingResponse(
        sheet_width=sheet.width,
        sheet_height=sheet.height,
        sheet_area=sheet.area,
        placed_area=result.placed_area,
        waste_area=result.waste_area,
        utilization=result.utilization,
        placements=[
            PlacementResponse(
                part_name=placement.part.name,
                x=placement.x,
                y=placement.y,
                width=placement.width,
                height=placement.height,
                rotated=placement.rotated,
            )
            for placement in result.placements
        ],
        unplaced_parts=[
            CuttingPartRequest(
                name=part.name,
                width=part.width,
                height=part.height,
                quantity=part.quantity,
            )
            for part in result.unplaced_parts
        ],
    )


@router.get(
    "/plans",
    response_model=list[CuttingPlanResponse],
)
def get_cutting_plans(
    db: Session = Depends(get_db),
):
    repository = CuttingPlanRepository(db)

    return repository.get_all()


@router.get(
    "/plans/{cutting_plan_id}",
    response_model=CuttingPlanResponse,
)
def get_cutting_plan(
    cutting_plan_id: int,
    db: Session = Depends(get_db),
):
    repository = CuttingPlanRepository(db)

    cutting_plan = repository.get_by_id(
        cutting_plan_id
    )

    if cutting_plan is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cutting plan not found",
        )

    return cutting_plan