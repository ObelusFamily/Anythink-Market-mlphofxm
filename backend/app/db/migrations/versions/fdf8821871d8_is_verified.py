"""main tables

Revision ID: fdf8821871d8
Revises:

"""
from typing import Tuple

import sqlalchemy as sa
from alembic import op
from sqlalchemy import func

revision = "fdf8821871d8"
down_revision = "fdf8821871d7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", 
        sa.Column("is_verified", sa.Boolean, server_default="False"),
    )


def downgrade() -> None:
    op.drop_column("users", "is_verified")
