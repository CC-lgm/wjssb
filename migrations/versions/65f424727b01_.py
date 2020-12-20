"""empty message

Revision ID: 65f424727b01
Revises: 4a6e461fe927
Create Date: 2020-12-15 05:22:13.312294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65f424727b01'
down_revision = '4a6e461fe927'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('signers', sa.Column('signer_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'signers', 'users', ['signer_id'], ['id'])
    op.add_column('users', sa.Column('signer_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'signers', ['signer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'signer_id')
    op.drop_constraint(None, 'signers', type_='foreignkey')
    op.drop_column('signers', 'signer_id')
    # ### end Alembic commands ###