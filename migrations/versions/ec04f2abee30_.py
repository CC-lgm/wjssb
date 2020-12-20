"""empty message

Revision ID: ec04f2abee30
Revises: 2f96d530ca73
Create Date: 2020-12-17 01:47:55.764385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec04f2abee30'
down_revision = '2f96d530ca73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('sign_status', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('sign_time_total', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'sign_time_total')
    op.drop_column('users', 'sign_status')
    # ### end Alembic commands ###