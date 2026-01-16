from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Part(Base):
    __tablename__ = "parts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    drawing_number: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(200),
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
        default=1,
    )

    material_id: Mapped[int] = mapped_column(
        ForeignKey("materials.id"),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    material = relationship(
        "Material",
        back_populates="parts",
    )