from alembic import op
import sqlalchemy as sa

from gabby.database_utils import sql_create_exercise_number_collation, sql_drop_exercise_number_collation


revision = "2816939acb1c"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(sql_create_exercise_number_collation)
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "adaptations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("kind", sa.String(length=16), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "pdf_files",
        sa.Column("sha256", sa.String(), nullable=False),
        sa.Column("bytes_count", sa.Integer(), nullable=False),
        sa.Column("pages_count", sa.Integer(), nullable=False),
        sa.CheckConstraint("regexp_like(sha256, '^[0-9a-f]{64}$')", name="check_sha256_format"),
        sa.PrimaryKeyConstraint("sha256"),
    )
    op.create_table(
        "projects",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(), nullable=True),
        sa.Column("hashed_password", sa.String(), nullable=True),
        sa.CheckConstraint("regexp_like(username, '^[-_A-Za-z0-9]+$')", name="check_username"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "adaptations__fwft",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("placeholder", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"],
            ["adaptations.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "adaptations__g",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"],
            ["adaptations.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "adaptations__mcii",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("placeholder", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"],
            ["adaptations.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "adaptations__mciw",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"],
            ["adaptations.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "adaptations__st",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("punctuation", sa.Boolean(), nullable=False),
        sa.Column("words", sa.Boolean(), nullable=False),
        sa.Column("colors", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"],
            ["adaptations.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "pdf_file_namings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("pdf_file_sha256", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["pdf_file_sha256"],
            ["pdf_files.sha256"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "pings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("message", sa.String(), nullable=True),
        sa.Column("prev_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("created_by_id", sa.Integer(), nullable=True),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_by_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["prev_id"],
            ["pings.id"],
        ),
        sa.ForeignKeyConstraint(
            ["updated_by_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "textbooks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("publisher", sa.String(), nullable=True),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("isbn", sa.String(), nullable=True),
        sa.CheckConstraint("regexp_like(isbn, '^[0-9]+$')", name="check_isbn_format"),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id", "project_id"),
    )
    op.create_table(
        "user_email_addresses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("address", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("address"),
    )
    op.create_table(
        "exercises",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("textbook_id", sa.Integer(), nullable=True),
        sa.Column("textbook_page", sa.Integer(), nullable=True),
        sa.Column("bounding_rectangle", sa.JSON(), nullable=True),
        sa.Column("number", sa.String(collation="exercise_number"), nullable=False),
        sa.Column("instructions", sa.String(), nullable=False),
        sa.Column("wording", sa.String(), nullable=False),
        sa.Column("example", sa.String(), nullable=False),
        sa.Column("clue", sa.String(), nullable=False),
        sa.Column("adaptation_id", sa.Integer(), nullable=True),
        sa.CheckConstraint(
            "(textbook_id IS NULL) = (textbook_page IS NULL)", name="textbook_id_textbook_page_consistently_null"
        ),
        sa.ForeignKeyConstraint(
            ["adaptation_id"],
            ["adaptations.id"],
        ),
        sa.ForeignKeyConstraint(
            ["project_id", "textbook_id"],
            ["textbooks.project_id", "textbooks.id"],
        ),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("adaptation_id"),
        sa.UniqueConstraint("textbook_id", "textbook_page", "number"),
    )
    op.create_table(
        "sections",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("textbook_id", sa.Integer(), nullable=False),
        sa.Column("pdf_file_sha256", sa.String(), nullable=False),
        sa.Column("textbook_start_page", sa.Integer(), nullable=False),
        sa.Column("pdf_file_start_page", sa.Integer(), nullable=False),
        sa.Column("pages_count", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["pdf_file_sha256"],
            ["pdf_files.sha256"],
        ),
        sa.ForeignKeyConstraint(
            ["textbook_id"],
            ["textbooks.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "extraction_events",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("exercise_id", sa.Integer(), nullable=False),
        sa.Column("event", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["exercise_id"],
            ["exercises.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("extraction_events")
    op.drop_table("sections")
    op.drop_table("exercises")
    op.drop_table("user_email_addresses")
    op.drop_table("textbooks")
    op.drop_table("pings")
    op.drop_table("pdf_file_namings")
    op.drop_table("adaptations__st")
    op.drop_table("adaptations__mciw")
    op.drop_table("adaptations__mcii")
    op.drop_table("adaptations__g")
    op.drop_table("adaptations__fwft")
    op.drop_table("users")
    op.drop_table("projects")
    op.drop_table("pdf_files")
    op.drop_table("adaptations")
    # ### end Alembic commands ###
    op.execute(sql_drop_exercise_number_collation)
