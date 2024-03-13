"""empty message

Revision ID: 50331b3c39bb
Revises: 77c100300b5b
Create Date: 2023-04-06 22:08:12.511699

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '50331b3c39bb'
down_revision = '77c100300b5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'cache',
        'file_size',
        existing_type=sa.INTEGER(),
        type_=sa.BigInteger(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'cache',
        'file_size',
        existing_type=sa.BigInteger(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    # ### end Alembic commands ###
