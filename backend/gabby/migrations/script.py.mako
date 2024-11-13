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
            adaptation = exercise._adaptation
            assert adaptation["format"] == 2
            settings = adaptation["settings"]
            kind = settings["kind"]
            if kind is None or kind == "select-things":
                kind = "generic"
            effects = []
            for effect in settings["effects"]:
                if effect["kind"] == "select-things":
                    assert effect["words"]

                    effect = dict(
                        kind="items-and-effects-attempt-1",
                        items=dict(
                            kind="words",
                            punctuation=effect["punctuation"],
                        ),
                        effects=dict(
                            selectable=dict(
                                colors=effect["colors"],
                            ),
                            boxed=False,
                        ),
                    )
                if effect["kind"] == "items-and-effects-attempt-1":
                    effect["kind"] = "itemized"
                effects.append(effect)
            exercise._adaptation = dict(format=2, settings=dict(kind=kind, effects=effects))
        session.commit()


def downgrade():
    ${downgrades if downgrades else "pass"}
