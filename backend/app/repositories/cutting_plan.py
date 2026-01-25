from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.cutting_plan import CuttingPlan


class CuttingPlanRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[CuttingPlan]:
        statement = select(CuttingPlan).order_by(
            CuttingPlan.id.desc()
        )

        return list(
            self.db.scalars(statement).all()
        )

    def get_by_id(
        self,
        cutting_plan_id: int,
    ) -> CuttingPlan | None:
        statement = select(CuttingPlan).where(
            CuttingPlan.id == cutting_plan_id
        )

        return self.db.scalar(statement)

    def create(
        self,
        material_id: int,
        used_area: float,
        waste_area: float,
        utilization: float,
    ) -> CuttingPlan:
        cutting_plan = CuttingPlan(
            material_id=material_id,
            used_area=used_area,
            waste_area=waste_area,
            utilization=utilization,
        )

        self.db.add(cutting_plan)
        self.db.commit()
        self.db.refresh(cutting_plan)

        return cutting_plan