from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class CuttingPlan(Base):
    __tablename__ = "cutting_plans"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    material_id: Mapped[int] = mapped_column(
        ForeignKey("materials.id"),
        nullable=False,
    )

    used_area: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    waste_area: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    utilization: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    material = relationship(
        "Material",
        back_populates="cutting_plans",
    )