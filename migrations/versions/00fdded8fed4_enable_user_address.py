# Revision ID: 00fdded8fed4
# Revises:
# Create Date: 2022-04-21 11:49:4,7.979440

"""
Enable user remote address tracking

This migration adds a new column 'remote_address' to the 'user' table to store the remote address of each user.
"""

from alembic import op
import sqlalchemy as sa


def upgrade():
    """
    Add 'remote_address' column to 'user' table
    """
    op.add_column("user", sa.Column("remote_address", sa.String(), nullable=True))


def downgrade():
    """
    Remove 'remote_address' column from 'user' table
    """
    op.drop_column("user", "remote_address")
