"""Adding new models

Revision ID: 3d6b4e815560
Revises: 6fa615b10581
Create Date: 2025-02-11 18:20:10.683849

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d6b4e815560'
down_revision: Union[str, None] = '6fa615b10581'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apartments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('number_of_people', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_apartments_id'), 'apartments', ['id'], unique=False)
    op.create_table('apartment_calendar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('apartment_id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.CheckConstraint('end_date > start_date', name='check_end_after_start'),
    sa.ForeignKeyConstraint(['apartment_id'], ['apartments.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_apartment_calendar_id'), 'apartment_calendar', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_apartment_calendar_id'), table_name='apartment_calendar')
    op.drop_table('apartment_calendar')
    op.drop_index(op.f('ix_apartments_id'), table_name='apartments')
    op.drop_table('apartments')
    # ### end Alembic commands ###
