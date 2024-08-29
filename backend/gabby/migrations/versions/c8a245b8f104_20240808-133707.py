from alembic import op
import sqlalchemy as sa


revision = "c8a245b8f104"
down_revision = "0be827860b2d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("exercises", sa.Column("rectangles", sa.JSON(), server_default="[]", nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("exercises", "rectangles")
    # ### end Alembic commands ###
