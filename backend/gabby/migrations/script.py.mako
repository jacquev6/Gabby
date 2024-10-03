from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm
${imports if imports else ""}

from gabby.exercises import Exercise


revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade():
    ${upgrades if upgrades else "pass"}
    with orm.Session(op.get_bind()) as session:
        for exercise in session.query(Exercise).all():
            exercise.adaptation = exercise.adaptation
        session.commit()


def downgrade():
    ${downgrades if downgrades else "pass"}
