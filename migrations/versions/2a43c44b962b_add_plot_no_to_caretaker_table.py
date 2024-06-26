"""add plot-no to caretaker table

Revision ID: 2a43c44b962b
Revises: 
Create Date: 2024-03-26 00:37:55.198230

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a43c44b962b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('care-taker', sa.Column('plot_no', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('care-taker', 'plot_no')
    # ### end Alembic commands ###
