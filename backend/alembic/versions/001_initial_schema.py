"""create initial database schema

Revision ID: 001_initial_schema
Revises:
Create Date: 2026-08-28
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "001_initial_schema"
down_revision: Union[str, Sequence[str], None] = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "materials",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("grade", sa.String(100), nullable=False),
        sa.Column("thickness", sa.Float(), nullable=False),
        sa.Column("width", sa.Float(), nullable=False),
        sa.Column("height", sa.Float(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("created_at", sa.DateTime(), nullable=False),
    )

    op.create_table(
        "parts",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("drawing_number", sa.String(100), nullable=False),
        sa.Column("name", sa.String(200), nullable=False),
        sa.Column("width", sa.Float(), nullable=False),
        sa.Column("height", sa.Float(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("material_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["material_id"],
            ["materials.id"],
        ),
    )

    op.create_table(
        "cutting_plans",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("material_id", sa.Integer(), nullable=False),
        sa.Column("sheet_id", sa.Integer(), nullable=False),
        sa.Column("used_area", sa.Float(), nullable=False),
        sa.Column("waste_area", sa.Float(), nullable=False),
        sa.Column("utilization", sa.Float(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["material_id"],
            ["materials.id"],
        ),
    )


def downgrade() -> None:
    op.drop_table("cutting_plans")
    op.drop_table("parts")
    op.drop_table("materials")