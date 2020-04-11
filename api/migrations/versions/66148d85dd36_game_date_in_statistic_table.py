"""Game date in Statistic table

Revision ID: 66148d85dd36
Revises: f5b82fbf5110
Create Date: 2020-04-11 17:53:30.679380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66148d85dd36'
down_revision = 'f5b82fbf5110'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('statistic', sa.Column('game_finished', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('statistic', 'game_finished')
    # ### end Alembic commands ###
