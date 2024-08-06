import json
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
