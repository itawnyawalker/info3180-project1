"""empty message

Revision ID: 8a6f27cb2ccc
Revises: e967055c37d9
Create Date: 2022-03-20 18:23:45.843084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a6f27cb2ccc'
down_revision = 'e967055c37d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('num_bedrooms', sa.Integer(), nullable=True),
    sa.Column('num_bathrooms', sa.Float(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('ptype', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('photo', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property_info')
    # ### end Alembic commands ###
