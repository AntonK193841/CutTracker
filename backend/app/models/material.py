from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Material(Base):
    __tablename__ = "materials"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    grade: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    thickness: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    width: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    height: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    parts = relationship(
        "Part",
        back_populates="material",
    )

    cutting_plans = relationship(
        "CuttingPlan",
        back_populates="material",
    )