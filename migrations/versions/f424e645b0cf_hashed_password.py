"""hashed_password

Revision ID: f424e645b0cf
Revises: ebbc675886a9
Create Date: 2023-09-12 23:08:06.997696

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "f424e645b0cf"
down_revision = "ebbc675886a9"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("hashed_password", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "hashed_password")
    # ### end Alembic commands ###