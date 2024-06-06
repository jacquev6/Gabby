import json
from urllib.parse import urlparse
import datetime
import io
import os
import subprocess
import sys
import tarfile

from sqlalchemy import orm
import boto3
import click
import sqlalchemy_data_model_visualizer

from . import database_utils
from . import orm_models
from . import settings
from .fixtures import load as load_fixtures


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


@main.command(help="Import data from a Django './manage.py dumpdata textbooks' JSON file")
@click.argument("input_file", type=click.File("r"))
def import_django_data(input_file):
    database_engine = database_utils.create_engine(settings.DATABASE_URL)

    last_pk_by_model = {}
    def assert_pk(model, pk):
        assert isinstance(pk, int)
        last_pk_by_model.setdefault(model, 0)
        assert pk > last_pk_by_model[model]  # Not always 'last_pk_by_model[model] + 1'
        last_pk_by_model[model] = pk

    data = json.load(input_file)

    instances_by_model = {}
    exercises_by_adaptation = {}

    with orm.Session(database_engine) as session:
        database_utils.truncate_all_tables(session)
        for instance_data in data:
            assert instance_data.keys() == {"model", "pk", "fields"}
            model = instance_data["model"]
            pk = instance_data["pk"]
            fields = instance_data["fields"]
            instance = None
            match model:
                case "textbooks.pdffile":
                    assert isinstance(pk, str)
                    assert len(pk) == 64
                    assert fields.keys() == {"bytes_count", "pages_count"}, fields
                    instance = orm_models.PdfFile(
                        sha256=pk,
                        bytes_count=fields.pop("bytes_count"),
                        pages_count=fields.pop("pages_count"),
                    )
                case "textbooks.pdffilenaming":
                    assert_pk(model, pk)
                    assert fields.keys() == {"pdf_file", "name"}, fields
                    instance = orm_models.PdfFileNaming(
                        pdf_file=instances_by_model["textbooks.pdffile"][fields.pop("pdf_file")],
                        name=fields.pop("name"),
                    )
                case "textbooks.project":
                    assert_pk(model, pk)
                    assert fields.keys() == {"title", "description"}, fields
                    instance = orm_models.Project(
                        title=fields.pop("title"),
                        description=fields.pop("description"),
                    )
                case "textbooks.textbook":
                    assert_pk(model, pk)
                    assert fields.keys() == {"project", "title", "publisher", "year", "isbn"}, fields
                    instance = orm_models.Textbook(
                        project=instances_by_model["textbooks.project"][fields.pop("project")],
                        title=fields.pop("title"),
                        publisher=fields.pop("publisher"),
                        year=fields.pop("year"),
                        isbn=fields.pop("isbn"),
                    )
                case "textbooks.section":
                    assert_pk(model, pk)
                    assert fields.keys() == {"textbook", "pdf_file", "textbook_start_page", "pdf_file_start_page", "pages_count"}, fields
                    instance = orm_models.Section(
                        textbook=instances_by_model["textbooks.textbook"][fields.pop("textbook")],
                        pdf_file=instances_by_model["textbooks.pdffile"][fields.pop("pdf_file")],
                        textbook_start_page=fields.pop("textbook_start_page"),
                        pdf_file_start_page=fields.pop("pdf_file_start_page"),
                        pages_count=fields.pop("pages_count"),
                    )
                case "textbooks.adaptation":
                    assert_pk(model, pk)
                    assert fields.keys() == {"polymorphic_ctype"}, fields
                case "textbooks.exercise":
                    assert_pk(model, pk)
                    assert fields.keys() == {"project", "textbook", "textbook_page", "bounding_rectangle", "number", "instructions", "wording", "example", "clue", "adaptation"}, fields
                    instance = orm_models.Exercise(
                        project=instances_by_model["textbooks.project"][fields.pop("project")],
                        textbook=None if (textbook := fields.pop("textbook")) is None else instances_by_model["textbooks.textbook"][textbook],
                        textbook_page=fields.pop("textbook_page"),
                        bounding_rectangle=fields.pop("bounding_rectangle"),
                        number=fields.pop("number"),
                        instructions=fields.pop("instructions"),
                        wording=fields.pop("wording"),
                        example=fields.pop("example"),
                        clue=fields.pop("clue"),
                        adaptation=None,
                    )
                    exercises_by_adaptation[fields.pop("adaptation")] = instance
                case "textbooks.extractionevent":
                    assert_pk(model, pk)
                    assert fields.keys() == {"exercise", "event"}, fields
                    instance = orm_models.ExtractionEvent(
                        exercise=instances_by_model["textbooks.exercise"][fields.pop("exercise")],
                        event=fields.pop("event"),
                    )
                case "textbooks.selectthingsadaptation":
                    assert_pk(model, pk)
                    assert fields.keys() == {"punctuation", "words", "colors"}, fields
                    instance = orm_models.SelectThingsAdaptation(
                        punctuation=fields.pop("punctuation"),
                        words=fields.pop("words"),
                        colors=fields.pop("colors"),
                    )
                    exercises_by_adaptation.pop(pk).adaptation = instance
                case "textbooks.fillwithfreetextadaptation":
                    assert_pk(model, pk)
                    assert fields.keys() == {"placeholder"}, fields
                    instance = orm_models.FillWithFreeTextAdaptation(
                        placeholder=fields.pop("placeholder"),
                    )
                    exercises_by_adaptation.pop(pk).adaptation = instance
                case "textbooks.multiplechoicesadaptation":
                    assert_pk(model, pk)
                    assert fields.keys() == {"placeholder"}, fields
                    instance = orm_models.MultipleChoicesInInstructionsAdaptation(
                        placeholder=fields.pop("placeholder"),
                    )
                    exercises_by_adaptation.pop(pk).adaptation = instance
                case _:
                    assert False, model
            if instance is None:
                assert model == "textbooks.adaptation", model
            else:
                assert fields == {}, fields
                session.add(instance)
                instances_by_model.setdefault(model, {})[pk] = instance
        exercises_by_adaptation.pop(None)
        assert exercises_by_adaptation == {}, exercises_by_adaptation
        session.commit()


@main.command(name="load-fixtures")
@click.argument("fixtures", nargs=-1)
def load_fixtures_(fixtures):
    database_engine = database_utils.create_engine(settings.DATABASE_URL)
    with orm.Session(database_engine) as session:
        load_fixtures(session, fixtures)
        session.commit()


if __name__ == "__main__":
    main()
