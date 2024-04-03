"""added note in data_about_documents

Revision ID: f417a14577f0
Revises: 347e0af5dd07
Create Date: 2024-04-02 14:07:44.334320

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f417a14577f0'
down_revision: Union[str, None] = '347e0af5dd07'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('data_about_documents', sa.Column('note', sa.String(length=300), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('data_about_documents', 'note')
    # ### end Alembic commands ###