import click

from .database_utils import create_tables, create_engine
from . import settings
from . import users, pings  # Not used directly but required to populate the metadata


@click.group()
def main():
    pass


@main.command
def migrate():
    print(f"Creating database at {settings.DATABASE_URL}...")
    create_tables(create_engine(settings.DATABASE_URL))


if __name__ == "__main__":
    main()
