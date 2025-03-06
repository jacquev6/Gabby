from alembic import op
import sqlalchemy as sa


revision = "466912d2351b"
down_revision = "c8a245b8f104"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("adaptations__st", "colors", new_column_name="old_colors_count")
    op.add_column("adaptations__st", sa.Column("colors", sa.JSON(), server_default='["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb", "#bbbbbb"]', nullable=False))


def downgrade():
    op.drop_column("adaptations__st", "colors")
    op.alter_column("adaptations__st", "old_colors_count", new_column_name="colors")
