from alembic import op
import sqlalchemy as sa
${imports if imports else ""}
from gabby.database_utils import sql_create_exercise_number_collation, sql_drop_exercise_number_collation


revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade():
    op.execute(sql_create_exercise_number_collation)
    ${upgrades if upgrades else "pass"}


def downgrade():
    ${downgrades if downgrades else "pass"}
    op.execute(sql_drop_exercise_number_collation)
