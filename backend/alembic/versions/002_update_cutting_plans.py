"""update cutting plans

Revision ID: 002_update_cutting_plans
Revises: 001_initial_schema
Create Date: 2026-01-25 
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "002_update_cutting_plans"
down_revision: Union[str, Sequence[str], None] = "001_initial_schema"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column(
        "cutting_plans",
        "sheet_id",
    )


def downgrade() -> None:
    op.add_column(
        "cutting_plans",
        sa.Column(
            "sheet_id",
            sa.Integer(),
            nullable=False,
            server_default="0",
        ),
    )