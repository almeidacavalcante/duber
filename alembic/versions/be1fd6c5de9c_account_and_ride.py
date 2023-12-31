"""account and ride

Revision ID: be1fd6c5de9c
Revises: 
Create Date: 2023-10-29 14:37:21.809249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be1fd6c5de9c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('account_id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('is_passenger', sa.Boolean(), nullable=False),
    sa.Column('is_driver', sa.Boolean(), nullable=False),
    sa.Column('car_plate', sa.String(length=7), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('verification_code', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('account_id')
    )
    op.create_table('rides',
    sa.Column('ride_id', sa.String(length=36), nullable=False),
    sa.Column('passenger_id', sa.String(length=36), nullable=False),
    sa.Column('driver_id', sa.String(length=36), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=False),
    sa.Column('fare', sa.Numeric(), nullable=True),
    sa.Column('distance', sa.Numeric(), nullable=True),
    sa.Column('from_lat', sa.Numeric(), nullable=False),
    sa.Column('from_long', sa.Numeric(), nullable=False),
    sa.Column('to_lat', sa.Numeric(), nullable=False),
    sa.Column('to_long', sa.Numeric(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['driver_id'], ['accounts.account_id'], ),
    sa.ForeignKeyConstraint(['passenger_id'], ['accounts.account_id'], ),
    sa.PrimaryKeyConstraint('ride_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rides')
    op.drop_table('accounts')
    # ### end Alembic commands ###
