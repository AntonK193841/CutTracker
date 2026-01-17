from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.part import PartRepository
from app.repositories.material import MaterialRepository
from app.schemas.part import (
    PartCreate,
    PartResponse,
)


router = APIRouter(
    prefix="/api/parts",
    tags=["Parts"],
)


@router.get(
    "",
    response_model=list[PartResponse],
)
def get_parts(
    db: Session = Depends(get_db),
):
    repository = PartRepository(db)

    return repository.get_all()


@router.get(
    "/{part_id}",
    response_model=PartResponse,
)
def get_part(
    part_id: int,
    db: Session = Depends(get_db),
):
    repository = PartRepository(db)

    part = repository.get_by_id(part_id)

    if part is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Part not found",
        )

    return part


@router.post(
    "",
    response_model=PartResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_part(
    data: PartCreate,
    db: Session = Depends(get_db),
):
    material_repository = MaterialRepository(db)

    material = material_repository.get_by_id(
        data.material_id
    )

    if material is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Material not found",
        )

    repository = PartRepository(db)

    return repository.create(data)


@router.delete(
    "/{part_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_part(
    part_id: int,
    db: Session = Depends(get_db),
):
    repository = PartRepository(db)

    part = repository.get_by_id(part_id)

    if part is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Part not found",
        )

    repository.delete(part)