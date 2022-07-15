"""Increased password character limit

Revision ID: 121b5b013fb9
Revises: b098bb518ca0
Create Date: 2022-07-14 17:14:46.033522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '121b5b013fb9'
down_revision = 'b098bb518ca0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=250),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.String(length=250),
               type_=sa.VARCHAR(length=20),
               existing_nullable=True)
    # ### end Alembic commands ###
