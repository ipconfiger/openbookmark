"""init bookmark

Revision ID: 1c51afad6486
Revises: 
Create Date: 2020-07-28 22:39:33.209535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c51afad6486'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookmark',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('domain', sa.String(length=100), nullable=True),
    sa.Column('base_url', sa.String(length=256), nullable=True),
    sa.Column('url', sa.String(length=512), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('image_url', sa.String(length=256), nullable=True),
    sa.Column('post_count', sa.Integer(), nullable=True),
    sa.Column('hidden', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookmark')
    # ### end Alembic commands ###
