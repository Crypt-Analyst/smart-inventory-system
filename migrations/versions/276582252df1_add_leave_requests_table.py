"""Add leave_requests table

Revision ID: 276582252df1
Revises: e926d7873ec5
Create Date: 2025-07-02 01:19:13.694209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '276582252df1'
down_revision = 'e926d7873ec5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leave_requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('employee_id', sa.Integer(), nullable=False),
    sa.Column('leave_type', sa.String(length=50), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('reason', sa.String(length=250), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('leave_requests')
    # ### end Alembic commands ###
