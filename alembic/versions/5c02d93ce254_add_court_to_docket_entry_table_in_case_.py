# type: ignore

"""add court to docket entry table in case needed for row-based-access

Revision ID: 5c02d93ce254
Revises: 400c04778408
Create Date: 2021-08-10 08:46:44.910568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c02d93ce254'
down_revision = '400c04778408'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('docket_entries', sa.Column('court', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('docket_entries', 'court')
    # ### end Alembic commands ###
