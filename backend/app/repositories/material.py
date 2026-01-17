from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.material import Material
from app.schemas.material import MaterialCreate


class MaterialRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[Material]:
        statement = select(Material).order_by(Material.id)

        return list(
            self.db.scalars(statement).all()
        )

    def get_by_id(self, material_id: int) -> Material | None:
        statement = select(Material).where(
            Material.id == material_id
        )

        return self.db.scalar(statement)

    def create(self, data: MaterialCreate) -> Material:
        material = Material(
            name=data.name,
            grade=data.grade,
            thickness=data.thickness,
            width=data.width,
            height=data.height,
            quantity=data.quantity,
        )

        self.db.add(material)
        self.db.commit()
        self.db.refresh(material)

        return material

    def delete(self, material: Material) -> None:
        self.db.delete(material)
        self.db.commit()