from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.part import Part
from app.schemas.part import PartCreate


class PartRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Part]:
        statement = select(Part).order_by(Part.id)

        return list(
            self.db.scalars(statement).all()
        )

    def get_by_id(self, part_id: int) -> Part | None:
        statement = select(Part).where(
            Part.id == part_id
        )

        return self.db.scalar(statement)

    def create(self, data: PartCreate) -> Part:
        part = Part(
            drawing_number=data.drawing_number,
            name=data.name,
            width=data.width,
            height=data.height,
            quantity=data.quantity,
            material_id=data.material_id,
        )

        self.db.add(part)
        self.db.commit()
        self.db.refresh(part)

        return part

    def delete(self, part: Part) -> None:
        self.db.delete(part)
        self.db.commit()