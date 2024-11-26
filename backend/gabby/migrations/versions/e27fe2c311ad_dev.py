from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm


from gabby import parsing
from gabby.exercises import Exercise


revision = "e27fe2c311ad"
down_revision = "7ef48883e57b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("exercises", "instructions", new_column_name="instructions_text", nullable=True)
    op.alter_column("exercises", "wording", new_column_name="wording_text", nullable=True)
    op.alter_column("exercises", "example", new_column_name="example_text", nullable=True)
    op.alter_column("exercises", "clue", new_column_name="clue_text", nullable=True)
    op.add_column("exercises", sa.Column("instructions", sa.JSON(), server_default='[{"insert": "\\n", "attributes": {}}]', nullable=False))
    op.add_column("exercises", sa.Column("wording", sa.JSON(), server_default='[{"insert": "\\n", "attributes": {}}]', nullable=False))
    op.add_column("exercises", sa.Column("example", sa.JSON(), server_default='[{"insert": "\\n", "attributes": {}}]', nullable=False))
    op.add_column("exercises", sa.Column("clue", sa.JSON(), server_default='[{"insert": "\\n", "attributes": {}}]', nullable=False))
    # ### end Alembic commands ###
    with orm.Session(op.get_bind()) as session:
        delta_maker = parsing.DeltaMaker()

        for i, exercise in enumerate(session.query(Exercise).all()):
            print(f"{i:4} Migrating exercise id={exercise.id}", flush=True)

            # Fix adaptation
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

            if exercise.id == 88:
                exercise._wording_text = exercise._wording_text.replace("{choices2|(|/||)|…|( … )}", "( … )")

            # Fix instructions, wording, etc.
            exercise.instructions = delta_maker.transform(parsing.instructions_parser.parse(exercise._instructions_text + "\n"))
            exercise.wording = delta_maker.transform(parsing.wording_parser.parse(exercise._wording_text + "\n"))
            exercise.example = delta_maker.transform(parsing.example_and_clue_parser.parse(exercise._example_text + "\n"))
            exercise.clue = delta_maker.transform(parsing.example_and_clue_parser.parse(exercise._clue_text + "\n"))

        session.commit()


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("exercises", "clue")
    op.drop_column("exercises", "example")
    op.drop_column("exercises", "wording")
    op.drop_column("exercises", "instructions")
    op.alter_column("exercises", "instructions_text", new_column_name="instructions")
    op.alter_column("exercises", "wording_text", new_column_name="wording")
    op.alter_column("exercises", "example_text", new_column_name="example")
    op.alter_column("exercises", "clue_text", new_column_name="clue")
    # ### end Alembic commands ###
