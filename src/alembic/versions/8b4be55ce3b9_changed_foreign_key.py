"""Changed foreign key

Revision ID: 8b4be55ce3b9
Revises: cfe497b7a4ab
Create Date: 2025-02-16 11:53:27.706359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8b4be55ce3b9'
down_revision: Union[str, None] = 'cfe497b7a4ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('apartments_user_id_fkey', 'apartments', type_='foreignkey')
    op.create_foreign_key(None, 'apartments', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'apartments', type_='foreignkey')
    op.create_foreign_key('apartments_user_id_fkey', 'apartments', 'apartments', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
