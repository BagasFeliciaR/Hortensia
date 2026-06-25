"""add approval fields

Revision ID: 561aac5b16c0
Revises: db743f679207
Create Date: 2026-06-26 04:35:05.113899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '561aac5b16c0'
down_revision: Union[str, Sequence[str], None] = 'db743f679207'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "jobs",
        sa.Column(
            "approval_required",
            sa.Boolean(),
            nullable=False,
            server_default=sa.false(),
        ),
    )

    op.add_column(
        "jobs",
        sa.Column(
            "approved",
            sa.Boolean(),
            nullable=True,
        ),
    )

    op.alter_column(
        "jobs",
        "approval_required",
        server_default=None,
    )
