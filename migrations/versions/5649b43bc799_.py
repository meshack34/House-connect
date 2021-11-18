"""empty message

Revision ID: 5649b43bc799
Revises: de53a58e69d8
Create Date: 2021-11-18 20:53:23.319120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5649b43bc799'
down_revision = 'de53a58e69d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('homes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=15), nullable=True),
    sa.Column('number_of_rooms', sa.Integer(), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('homes')
    # ### end Alembic commands ###
