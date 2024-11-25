from urllib.parse import urlparse
import datetime
import io
import os
import re
import subprocess
import sys
import tarfile

from sqlalchemy import orm
import boto3
import click
import sqlalchemy as sql
import sqlalchemy_data_model_visualizer
import sqlalchemy_utils.functions

from . import database_utils
from . import orm_models
from . import settings
from .fixtures import load as load_fixtures
from . import renderable
from . import exercise_delta


@click.group()
def main():
    pass


@main.command()
def graph_models():
    sqlalchemy_data_model_visualizer.generate_data_model_diagram(orm_models.all_models, "gabby/orm_models", add_labels=True)
    os.unlink("gabby/orm_models")


parsed_database_url = urlparse(settings.DATABASE_URL)
assert parsed_database_url.scheme == "postgresql+psycopg2"

parsed_database_backups_url = urlparse(settings.DATABASE_BACKUPS_URL)

@main.command()
def backup_database():
    now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_name = f"gabby-backup-{now}"
    archive_name = f"{backup_name}.tar.gz"

    print(f"Backing up database {settings.DATABASE_URL} to {settings.DATABASE_BACKUPS_URL}/{archive_name}", file=sys.stderr)

    pg_dump = subprocess.run(
        [
            "pg_dump",
            "--host", parsed_database_url.hostname,
            "--username", parsed_database_url.username,
            "--no-password",
            "--dbname", parsed_database_url.path[1:],
            "--file", "-",
            "--create", "--column-inserts", "--quote-all-identifiers",
        ],
        env=dict(os.environ, PGPASSWORD=parsed_database_url.password),
        check=True,
        capture_output=True,
    )

    def populate_tarball(tarball):
        info = tarfile.TarInfo(f"{backup_name}/pg_dump.sql")
        info.size = len(pg_dump.stdout)
        tarball.addfile(info, io.BytesIO(pg_dump.stdout))

    if parsed_database_backups_url.scheme == "file":
        with tarfile.open(os.path.join(parsed_database_backups_url.path, archive_name), "w:gz") as tarball:
            populate_tarball(tarball)
    elif parsed_database_backups_url.scheme == "s3":
        assert "AWS_ACCESS_KEY_ID" in os.environ
        assert "AWS_SECRET_ACCESS_KEY" in os.environ
        s3 = boto3.client("s3")
        buffer = io.BytesIO()
        with tarfile.open(fileobj=buffer, mode="w:gz") as tarball:
            populate_tarball(tarball)
        buffer.seek(0)
        s3.upload_fileobj(buffer, parsed_database_backups_url.netloc, f"{parsed_database_backups_url.path[1:]}/{archive_name}")
    else:
        raise NotImplementedError(f"Unsupported database backup URL scheme: {parsed_database_backups_url.scheme}")

    print(f"Backed up database {settings.DATABASE_URL} to {settings.DATABASE_BACKUPS_URL}/{archive_name}", file=sys.stderr)


@main.command()
@click.argument("backup_url")
@click.option("--yes", is_flag=True)
@click.option("--patch-according-to-settings", is_flag=True)
def restore_database(backup_url, yes, patch_according_to_settings):
    parsed_backup_url = urlparse(backup_url)

    if parsed_backup_url.scheme == "file":
        with tarfile.open(parsed_backup_url.path, "r:gz") as tarball:
            pg_dump = tarball.extractfile(tarball.getnames()[0]).read()
    elif parsed_backup_url.scheme == "s3":
        assert "AWS_ACCESS_KEY_ID" in os.environ
        assert "AWS_SECRET_ACCESS_KEY" in os.environ
        s3 = boto3.client("s3")
        buffer = io.BytesIO()
        s3.download_fileobj(parsed_backup_url.netloc, f"{parsed_backup_url.path[1:]}", buffer)
        buffer.seek(0)
        with tarfile.open(fileobj=buffer, mode="r:gz") as tarball:
            pg_dump = tarball.extractfile(tarball.getnames()[0]).read()
    else:
        raise NotImplementedError(f"Unsupported database backup URL scheme: {parsed_database_backups_url.scheme}")

    print(f"Restoring database {settings.DATABASE_URL} from {backup_url} ({len(pg_dump)} bytes)", file=sys.stderr)
    if not yes:
        print("This will overwrite the current database. Are you sure you want to continue? [y/N]", file=sys.stderr, end=" ")
        if input().strip().lower() != "y":
            print("Aborting.", file=sys.stderr)
            return

    placeholder_database_url = settings.DATABASE_URL + "-restore"
    if not sqlalchemy_utils.functions.database_exists(placeholder_database_url):
        sqlalchemy_utils.functions.create_database(placeholder_database_url)
    parsed_placeholder_database_url = urlparse(placeholder_database_url)

    if sqlalchemy_utils.functions.database_exists(settings.DATABASE_URL):
        sqlalchemy_utils.functions.drop_database(settings.DATABASE_URL)

    sql = pg_dump.decode()
    if patch_according_to_settings:
        # Comments
        sql = re.sub(r" Owner: \w+", f" Owner: {parsed_database_url.username}", sql)
        sql = re.sub(r"-- Name: \w+; Type: DATABASE;", f"-- Name: {parsed_database_url.path[1:]}; Type: DATABASE;", sql)
        # Postgres commands
        sql = re.sub(r"connect \"\w+\"", f"connect \"{parsed_database_url.path[1:]}\"", sql)
        # Actual SQL
        sql = re.sub(r" OWNER TO \"\w+\";", f" OWNER TO \"{parsed_database_url.username}\";", sql)
        sql = re.sub(r"DATABASE \"\w+\"", f"DATABASE \"{parsed_database_url.path[1:]}\"", sql)

    subprocess.run(
        [
            "psql",
            "--host", parsed_placeholder_database_url.hostname,
            "--username", parsed_placeholder_database_url.username,
            "--no-password",
            "--dbname", parsed_placeholder_database_url.path[1:],
        ],
        env=dict(os.environ, PGPASSWORD=parsed_placeholder_database_url.password),
        check=True,
        input=sql,
        universal_newlines=True,
    )

    sqlalchemy_utils.functions.drop_database(placeholder_database_url)


@main.command()
def check_database_with_orm():
    database_engine = database_utils.create_engine(settings.DATABASE_URL)
    ok = True
    with orm.Session(database_engine) as session:
        for exercise in session.query(orm_models.Exercise):
            try:
                exercise.adaptation
                exercise.make_adapted_and_delta()
                print("Exercise", exercise.id, "OK", file=sys.stderr)  # @todo Improve duration (currently 0.3s / exercise) and remove this progress log
            except Exception as e:
                print(f"ERROR with exercise {exercise.id}: {e}", file=sys.stderr)
                ok = False
    if not ok:
        sys.exit(1)


@main.command()
def dump_database_as_unit_tests():
    # Waste data to avoid issues with copyrighted material (extracted from textbooks)
    def waste_char(c):
        return {
            # Keep "abcdef" unchanged for lists (hoping no list is longer than 6 items)
            # Keep "ou" unchanged for French separator2
            "I": "A", "Y": "A",
            "G": "B", "H": "F", "J": "B", "K": "F", "L": "B", "M": "B", "N": "B", "P": "F", "Q": "B", "R": "B", "S": "C", "T": "B", "V": "F", "W": "F", "X": "B", "Z": "C",
            "i": "a", "y": "a",
            "g": "b", "h": "f", "j": "b", "k": "f", "l": "b", "m": "b", "n": "b", "p": "f", "q": "b", "r": "b", "s": "c", "t": "b", "v": "f", "w": "f", "x": "b", "z": "c",
        }.get(c, c)

    tags = [
        ("".join(waste_char(c) for c in tag), tag)
        for tag in ["{choices2|", "{bold|", "{italic|", "{sel1|", "{sel2|", "{sel3|", "{sel4|", "{sel5|"]
    ]

    def waste_string(s):
        r = "".join(waste_char(c) for c in s)
        for wasted_tag, tag in tags:
            r = r.replace(wasted_tag, tag)
        return r

    def waste_renderable(section):
        def waste_token(token):
            return {
                "boxedText": lambda: renderable.BoxedText(text=waste_string(token.text)),
                "freeTextInput": lambda: renderable.FreeTextInput(),
                "multipleChoicesInput": lambda: renderable.MultipleChoicesInput(choices=[waste_string(choice) for choice in token.choices]),
                "plainText": lambda: renderable.PlainText(text=waste_string(token.text)),
                "selectableText": lambda: renderable.SelectableText(text=waste_string(token.text), colors=token.colors, boxed=token.boxed),
                "selectedText": lambda: renderable.SelectedText(text=waste_string(token.text), color=token.color),
                "whitespace": lambda: renderable.Whitespace(),
            }[token.type]()

        def waste_sentence(sentence):
            return renderable.Sentence(tokens=[waste_token(token) for token in sentence.tokens])

        def waste_paragraph(paragraph):
            return renderable.Paragraph(sentences=[waste_sentence(sentence) for sentence in paragraph.sentences])

        def waste_section(section):
            return renderable.Section(paragraphs=[waste_paragraph(paragraph) for paragraph in section.paragraphs])

        return waste_section(section)

    def waste_delta(delta):
        attributes = delta.attributes
        if "choices2" in attributes:
            attributes = {
                "choices2": {
                    k: waste_string(v)
                    for k, v in attributes["choices2"].items()
                }
            }
        return exercise_delta.TextInsertOp(
            insert=waste_string(delta.insert),
            attributes=attributes,
        )

    def waste_deltas(deltas):
        return [waste_delta(delta) for delta in deltas]

    def gen():
        yield "# WARNING: this file is generated (from database content). Manual changes will be lost."
        yield ""
        yield "from . import exercise_delta as d"
        yield "from . import exercises as e"
        yield "from . import renderable as r"
        yield "from .adaptation import AdaptationTestCase"
        yield "from .api_models import AdaptationV2, FillWithFreeTextAdaptationEffect, ItemizedAdaptationEffect"
        yield "from .exercise_delta import TextInsertOp"
        yield "from .renderable import Section, Paragraph, Sentence, _PlainText, _Whitespace, _FreeTextInput, _SelectableText, _BoxedText, _MultipleChoicesInput, _SelectedText"
        yield ""
        yield ""
        yield "WordsItems = ItemizedAdaptationEffect.WordsItems"
        yield "ManualItems = ItemizedAdaptationEffect.ManualItems"
        yield "Effects = ItemizedAdaptationEffect.Effects"
        yield "Selectable = ItemizedAdaptationEffect.Effects.Selectable"
        yield ""
        yield ""
        yield "class DatabaseAsUnitTests(AdaptationTestCase):"

        database_engine = database_utils.create_engine(settings.DATABASE_URL)
        with orm.Session(database_engine) as session:
            for i, exercise in enumerate(session.query(orm_models.Exercise).all()):
                print(f"{i:4} Generating unit test for exercise id={exercise.id}", file=sys.stderr)

                adapted, _deltas = exercise.make_adapted_and_delta()

                yield f"    def test_exercise_{exercise.id}(self):"
                yield f"        self.do_test("
                yield f"            e.Exercise("
                yield f"                number={repr(waste_string(exercise.number))},"
                yield f"                textbook_page={repr(exercise.textbook_page)},"
                yield f"                instructions={repr(waste_string(exercise.instructions))},"
                yield f"                wording={repr(waste_string(exercise.wording))},"
                yield f"                example={repr(waste_string(exercise.example))},"
                yield f"                clue={repr(waste_string(exercise.clue))},"
                yield f"                wording_paragraphs_per_pagelet={repr(exercise.wording_paragraphs_per_pagelet)},"
                yield f"                adaptation={repr(exercise.adaptation)},"
                yield f"            ),"
                yield f"            r.Exercise("
                yield f"                number={repr(waste_string(exercise.number))},"
                yield f"                textbook_page={repr(exercise.textbook_page)},"
                yield f"                instructions={repr(waste_renderable(adapted.instructions))},"
                yield f"                wording={repr(waste_renderable(adapted.wording))},"
                yield f"                example={repr(waste_renderable(adapted.example))},"
                yield f"                clue={repr(waste_renderable(adapted.clue))},"
                yield f"                wording_paragraphs_per_pagelet={repr(exercise.wording_paragraphs_per_pagelet)},"
                yield f"            ),"
                yield f"            d.Exercise("
                yield f"                instructions={repr(waste_deltas(exercise.instructions_deltas))},"
                yield f"                wording={repr(waste_deltas(exercise.wording_deltas))},"
                yield f"                example={repr(waste_deltas(exercise.example_deltas))},"
                yield f"                clue={repr(waste_deltas(exercise.clue_deltas))},"
                yield f"            ),"
                yield f"        )"
                yield f""

    for line in gen():
        print(line)


@main.command(name="load-fixtures")
@click.argument("fixtures", nargs=-1)
def load_fixtures_(fixtures):
    database_engine = database_utils.create_engine(settings.DATABASE_URL)
    with orm.Session(database_engine) as session:
        load_fixtures(session, fixtures)
        session.commit()


@main.group()
@click.pass_context
@click.argument("username")
def sudo(context, username):
    context.obj = {"username": username}


@sudo.command()
@click.pass_context
@click.argument("email_address")
@click.option("--username", required=False)
@click.option("--password", required=False)
def create_user(context, email_address, username, password):
    database_engine = database_utils.create_engine(settings.DATABASE_URL)
    with orm.Session(database_engine) as session:
        sudo_user = session.scalar(sql.select(orm_models.User).where(orm_models.User.username == context.obj["username"]))
        assert sudo_user is not None, f"No user with username {context.obj['username']}"
        new_user = orm_models.User(username=username, clear_text_password=password, created_by_id=sudo_user.id, updated_by_id=sudo_user.id)
        session.add(new_user)
        session.flush()
        session.add(orm_models.UserEmailAddress(user=new_user, address=email_address))
        session.commit()


if __name__ == "__main__":
    main()
