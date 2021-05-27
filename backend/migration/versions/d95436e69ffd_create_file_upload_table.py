"""create file_upload table

Revision ID: d95436e69ffd
Revises: 
Create Date: 2021-04-26 07:12:05.207225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd95436e69ffd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'file_upload',
        sa.Column('id', sa.Integer, primary_key=True),
    )


def downgrade():
    op.drop_table('file_upload')
