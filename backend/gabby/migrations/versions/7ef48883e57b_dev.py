from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision = "7ef48883e57b"
down_revision = "6630dab8fc14"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("exercises_adaptation_id_key", "exercises", type_="unique")
    op.drop_constraint("exercises_adaptation_id_fkey", "exercises", type_="foreignkey")
    op.drop_table("adaptations__st")
    op.drop_table("adaptations__iae1")
    op.drop_table("adaptations__fwft")
    op.drop_table("extraction_events")
    op.drop_table("adaptations__mciw")
    op.drop_table("adaptations__mcii")
    op.drop_table("adaptations__g")
    op.drop_table("adaptations")
    op.drop_column("exercises", "bounding_rectangle")
    op.drop_column("exercises", "adaptation_id")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "adaptations",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('adaptations_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("kind", sa.VARCHAR(length=16), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("created_by_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("updated_by_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(["created_by_id"], ["users.id"], name="adaptations_created_by_id_fkey"),
        sa.ForeignKeyConstraint(["updated_by_id"], ["users.id"], name="adaptations_updated_by_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="adaptations_pkey"),
        postgresql_ignore_search_path=False,
    )
    op.add_column("exercises", sa.Column("adaptation_id", sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column(
        "exercises",
        sa.Column("bounding_rectangle", postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    )
    op.create_foreign_key("exercises_adaptation_id_fkey", "exercises", "adaptations", ["adaptation_id"], ["id"])
    op.create_unique_constraint("exercises_adaptation_id_key", "exercises", ["adaptation_id"])
    op.create_table(
        "adaptations__g",
        sa.Column("id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(["id"], ["adaptations.id"], name="adaptations__g_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="adaptations__g_pkey"),
    )
    op.create_table(
        "adaptations__mcii",
        sa.Column("id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("placeholder", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(["id"], ["adaptations.id"], name="adaptations__mcii_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="adaptations__mcii_pkey"),
    )
    op.create_table(
        "adaptations__mciw",
        sa.Column("id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(["id"], ["adaptations.id"], name="adaptations__mciw_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="adaptations__mciw_pkey"),
    )
    op.create_table(
        "extraction_events",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("exercise_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("event", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("created_by_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("updated_by_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(["created_by_id"], ["users.id"], name="extraction_events_created_by_id_fkey"),
        sa.ForeignKeyConstraint(
            ["exercise_id"], ["exercises.id"], name="extraction_events_exercise_id_fkey", ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(["updated_by_id"], ["users.id"], name="extraction_events_updated_by_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="extraction_events_pkey"),
    )
    op.create_table(
        "adaptations__fwft",
        sa.Column("id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("placeholder", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(["id"], ["adaptations.id"], name="adaptations__fwft_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="adaptations__fwft_pkey"),
    )
    op.create_table(
        "adaptations__iae1",
        sa.Column("id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("items", postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False),
        sa.Column("effects", postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(["id"], ["adaptations.id"], name="adaptations__iae1_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="adaptations__iae1_pkey"),
    )
    op.create_table(
        "adaptations__st",
        sa.Column("id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("punctuation", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column("words", sa.BOOLEAN(), autoincrement=False, nullable=False),
        sa.Column("old_colors_count", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column(
            "colors",
            postgresql.JSON(astext_type=sa.Text()),
            server_default=sa.text('\'["#ffff00", "#ffc0cb", "#bbbbff", "#bbffbb", "#bbbbbb"]\'::json'),
            autoincrement=False,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["id"], ["adaptations.id"], name="adaptations__st_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="adaptations__st_pkey"),
    )
    # ### end Alembic commands ###
