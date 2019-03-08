"""empty message

Revision ID: d1cb570314a0
Revises: 8eacdca4ca7a
Create Date: 2018-08-27 15:12:36.723203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1cb570314a0'
down_revision = '8eacdca4ca7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('news', sa.Column('current_date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('news', 'current_date')
    # ### end Alembic commands ###
