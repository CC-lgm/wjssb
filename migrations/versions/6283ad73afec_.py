"""empty message

Revision ID: 6283ad73afec
Revises: 09d6ba94e4a5
Create Date: 2020-12-14 03:30:20.550426

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6283ad73afec'
down_revision = '09d6ba94e4a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('signers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('signer_class', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('sign_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_signers_name'), 'signers', ['name'], unique=False)
    op.add_column('users', sa.Column('s_class', sa.String(length=64), nullable=True))
    op.drop_column('users', 'location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('location', mysql.VARCHAR(length=64), nullable=True))
    op.drop_column('users', 's_class')
    op.drop_index(op.f('ix_signers_name'), table_name='signers')
    op.drop_table('signers')
    # ### end Alembic commands ###
