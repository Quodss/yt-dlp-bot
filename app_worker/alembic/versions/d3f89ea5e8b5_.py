"""empty message

Revision ID: d3f89ea5e8b5
Revises: da4a97a0fdb7
Create Date: 2022-06-07 19:35:23.098590

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'd3f89ea5e8b5'
down_revision = 'da4a97a0fdb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('yt_dlp_version', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'yt_dlp_version')
    # ### end Alembic commands ###
