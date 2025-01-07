import copy
import itertools
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm


from gabby.exercises import Exercise


revision = "33389ce52383"
down_revision = "e27fe2c311ad"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

    # Data migration
    with orm.Session(op.get_bind()) as session:
        for exercise in session.query(Exercise).all():
            for insert_operation in itertools.chain(exercise._instructions_deltas, exercise._wording_deltas, exercise._example_deltas, exercise._clue_deltas, exercise._text_reference):
                assert "selectable" not in insert_operation["attributes"], "Unhandled old 'selectable' attribute"  # None in real-life DB => don't need to migrate

            adaptation = copy.deepcopy(exercise._adaptation)
            for effect in adaptation["settings"]["effects"]:
                if effect["kind"] == "itemized":
                    if effect["items"]["kind"] == "words":
                        effect["items"] = {"kind": "tokens", "words": True, "punctuation": effect["items"]["punctuation"]}
            exercise._adaptation = adaptation
        session.commit()


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
