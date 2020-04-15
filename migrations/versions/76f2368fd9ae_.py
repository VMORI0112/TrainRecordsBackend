"""empty message

Revision ID: 76f2368fd9ae
Revises: cc45762d48e0
Create Date: 2020-04-15 19:07:50.356951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76f2368fd9ae'
down_revision = 'cc45762d48e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('train_data', sa.Column('employerId', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('train_data', 'employerId')
    # ### end Alembic commands ###
