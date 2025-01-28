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
from . import deltas


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

    def waste_string(s):
        return "".join(waste_char(c) for c in s)

    def waste_renderable(section):
        def waste_selectable_token(token):
            return renderable.Selectable(contents=[waste_token(content) for content in token.contents], colors=token.colors, boxed=token.boxed)

        def waste_token(token):
            return {
                "boxedText": lambda: renderable.BoxedText(text=waste_string(token.text)),
                "freeTextInput": lambda: renderable.FreeTextInput(),
                "multipleChoicesInput": lambda: renderable.MultipleChoicesInput(choices=[waste_string(choice) for choice in token.choices]),
                "plainText": lambda: renderable.PlainText(text=waste_string(token.text)),
                "selectableText": lambda: renderable.SelectableText(text=waste_string(token.text), colors=token.colors, boxed=token.boxed),
                "selectedText": lambda: renderable.SelectedText(text=waste_string(token.text), color=token.color),
                "whitespace": lambda: renderable.Whitespace(),
                "selectable": lambda: waste_selectable_token(token),
            }[token.type]()

        def waste_paragraph(paragraph):
            return renderable.Paragraph(tokens=[waste_token(token) for token in paragraph.tokens])

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
        return deltas.InsertOp(
            insert=waste_string(delta.insert),
            attributes=attributes,
        )

    def waste_deltas(deltas):
        return [waste_delta(delta) for delta in deltas]

    def gen():
        yield "# WARNING: this file is generated (from database content). Manual changes will be lost."
        yield ""
        yield "from . import exercises as e"
        yield "from . import renderable as r"
        yield "from .adaptation import AdaptationTestCase"
        yield "from .api_models import Adaptation, FillWithFreeTextAdaptationEffect, ItemizedAdaptationEffect"
        yield "from .deltas import InsertOp"
        yield "from .renderable import Section, Paragraph, _PlainText, _Whitespace, _FreeTextInput, _SelectableText, _BoxedText, _MultipleChoicesInput, _SelectedText, _Selectable"
        yield ""
        yield ""
        yield "CharactersItems = ItemizedAdaptationEffect.CharactersItems"
        yield "TokensItems = ItemizedAdaptationEffect.TokensItems"
        yield "SentencesItems = ItemizedAdaptationEffect.SentencesItems"
        yield "ManualItems = ItemizedAdaptationEffect.ManualItems"
        yield "Effects = ItemizedAdaptationEffect.Effects"
        yield "Selectable = ItemizedAdaptationEffect.Effects.Selectable"
        yield ""
        yield ""
        yield "class DatabaseAsUnitTests(AdaptationTestCase):"

        database_engine = database_utils.create_engine(settings.DATABASE_URL)
        with orm.Session(database_engine) as session:
            for exercise in session.query(orm_models.Exercise).order_by(orm_models.Exercise.id).all():
                adapted = exercise.make_adapted()

                yield f"    def test_exercise_{exercise.id}(self):"
                yield f"        self.do_test("
                yield f"            e.Exercise("
                yield f"                number={repr(waste_string(exercise.number))},"
                yield f"                textbook_page={repr(exercise.textbook_page)},"
                yield f"                instructions={repr(waste_deltas(exercise.instructions))},"
                yield f"                wording={repr(waste_deltas(exercise.wording))},"
                yield f"                example={repr(waste_deltas(exercise.example))},"
                yield f"                clue={repr(waste_deltas(exercise.clue))},"
                yield f"                text_reference={repr(waste_deltas(exercise.text_reference))},"
                yield f"                wording_paragraphs_per_pagelet={repr(exercise.wording_paragraphs_per_pagelet)},"
                yield f"                adaptation={repr(exercise.adaptation)},"
                yield f"            ),"
                yield f"            r.Exercise("
                yield f"                number={repr(waste_string(exercise.number))},"
                yield f"                textbook_page={repr(exercise.textbook_page)},"
                yield f"                pagelets=["
                for pagelet in adapted.pagelets:
                    yield f"                    r.Pagelet("
                    yield f"                        instructions={repr(waste_renderable(pagelet.instructions))},"
                    yield f"                        wording={repr(waste_renderable(pagelet.wording))},"
                    yield f"                    ),"
                yield f"                ],"
                yield f"            ),"
                yield f"        )"
                yield f""

    # Black does not have a Python API, so use it as a command-line tool.
    # https://black.readthedocs.io/en/stable/faq.html#does-black-have-an-api
    subprocess.run(["black", "--line-length", "120", "-"], universal_newlines=True, input="\n".join(gen()), check=True)


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
