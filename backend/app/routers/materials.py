from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.material import MaterialRepository
from app.schemas.material import (
    MaterialCreate,
    MaterialResponse,
)


router = APIRouter(
    prefix="/api/materials",
    tags=["Materials"],
)


@router.get(
    "",
    response_model=list[MaterialResponse],
)
def get_materials(
    db: Session = Depends(get_db),
):
    repository = MaterialRepository(db)

    return repository.get_all()


@router.get(
    "/{material_id}",
    response_model=MaterialResponse,
)
def get_material(
    material_id: int,
    db: Session = Depends(get_db),
):
    repository = MaterialRepository(db)

    material = repository.get_by_id(material_id)

    if material is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material not found",
        )

    return material


@router.post(
    "",
    response_model=MaterialResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_material(
    data: MaterialCreate,
    db: Session = Depends(get_db),
):
    repository = MaterialRepository(db)

    return repository.create(data)


@router.delete(
    "/{material_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_material(
    material_id: int,
    db: Session = Depends(get_db),
):
    repository = MaterialRepository(db)

    material = repository.get_by_id(material_id)

    if material is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Material not found",
        )

    repository.delete(material)