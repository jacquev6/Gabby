from logging.config import fileConfig

from alembic import context

from gabby import database_utils, settings
from gabby import users, pings  # Not used in this file but required to populate the metadata


if context.config.config_file_name is not None:
    fileConfig(context.config.config_file_name)


# @todo Remove (when Django is decommissioned)
def include_name(name, type_, parent_names):
    # print(name, type_, parent_names, flush=True)
    if type_ == "table":
        if name.startswith("auth_") or name.startswith("django_"):
            return False
    return True


assert not context.is_offline_mode()

connectable = database_utils.create_engine(settings.DATABASE_URL)

with connectable.connect() as connection:
    context.configure(
        connection=connection,
        target_metadata=database_utils.OrmBase.metadata,
        include_name=include_name,
    )
    with context.begin_transaction():
        context.run_migrations()
