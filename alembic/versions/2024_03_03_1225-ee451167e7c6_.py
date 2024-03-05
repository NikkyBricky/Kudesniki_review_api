"""empty message

Revision ID: ee451167e7c6
Revises: 7aee713a7761
Create Date: 2024-03-03 12:25:58.215016

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee451167e7c6'
down_revision: Union[str, None] = '7aee713a7761'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('github_nickname', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'github_nickname')
    # ### end Alembic commands ###
