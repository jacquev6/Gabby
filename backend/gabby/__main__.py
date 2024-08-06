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
import sqlalchemy as sql
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
def create_user(context, email_address, username):
    database_engine = database_utils.create_engine(settings.DATABASE_URL)
    with orm.Session(database_engine) as session:
        sudo_user = session.scalar(sql.select(orm_models.User).where(orm_models.User.username == context.obj["username"]))
        assert sudo_user is not None, f"No user with username {context.obj['username']}"
        new_user = orm_models.User(username=username, created_by_id=sudo_user.id, updated_by_id=sudo_user.id)
        session.add(new_user)
        session.flush()
        session.add(orm_models.UserEmailAddress(user=new_user, address=email_address))
        session.commit()


if __name__ == "__main__":
    main()
