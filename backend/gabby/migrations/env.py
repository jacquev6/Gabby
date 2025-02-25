from logging.config import fileConfig

from alembic import context

from gabby import database_utils, settings
from gabby import orm_models  # To populate the metadata


if context.config.config_file_name is not None:
    fileConfig(context.config.config_file_name)


assert not context.is_offline_mode()

connectable = database_utils.create_engine(settings.DATABASE_URL)

with connectable.connect() as connection:
    context.configure(connection=connection, target_metadata=database_utils.OrmBase.metadata)
    with context.begin_transaction():
        context.run_migrations()
