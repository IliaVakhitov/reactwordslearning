"""Rename column order to round_order

Revision ID: 952732aefde9
Revises: 2e68dca228c4
Create Date: 2020-05-05 14:25:35.958454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '952732aefde9'
down_revision = '2e68dca228c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_round', sa.Column('round_order', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_game_round_round_order'), 'game_round', ['round_order'], unique=False)
    op.drop_index('ix_game_round_order', table_name='game_round')
    op.drop_column('game_round', 'order')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('game_round', sa.Column('order', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_index('ix_game_round_order', 'game_round', ['order'], unique=False)
    op.drop_index(op.f('ix_game_round_round_order'), table_name='game_round')
    op.drop_column('game_round', 'round_order')
    # ### end Alembic commands ###
