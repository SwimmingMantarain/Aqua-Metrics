"""renamed UserMeets to UserMeet

Revision ID: 1ef3c66710a6
Revises: d891d3ad635c
Create Date: 2025-05-03 18:12:21.622476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ef3c66710a6'
down_revision = 'd891d3ad635c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_meets')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_meets',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('meet_url', sa.VARCHAR(length=255), nullable=False),
    sa.Column('meet_date', sa.DATE(), nullable=False),
    sa.Column('meet_course', sa.INTEGER(), nullable=False),
    sa.Column('meet_city', sa.VARCHAR(length=100), nullable=False),
    sa.Column('meet_name', sa.VARCHAR(length=100), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
