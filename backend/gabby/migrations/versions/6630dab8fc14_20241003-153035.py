from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm


from gabby.exercises import Exercise


revision = "6630dab8fc14"
down_revision = "466912d2351b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "adaptations__iae1",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("items", sa.JSON(), nullable=False),
        sa.Column("effects", sa.JSON(), nullable=False),
        sa.ForeignKeyConstraint(
            ["id"],
            ["adaptations.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column(
        "exercises", sa.Column("wording_paragraphs_per_pagelet", sa.Integer(), server_default="3", nullable=False)
    )
    op.add_column("exercises", sa.Column("adaptation", sa.JSON(), server_default='{"format": 0}', nullable=False))
    # ### end Alembic commands ###
    with orm.Session(op.get_bind()) as session:
        for exercise in session.query(Exercise).all():
            exercise.adaptation = exercise.adaptation
            # exercise.old_adaptation = None
        session.commit()


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("exercises", "adaptation")
    op.drop_column("exercises", "wording_paragraphs_per_pagelet")
    op.drop_table("adaptations__iae1")
    # ### end Alembic commands ###