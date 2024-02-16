import logging
from logging.config import fileConfig

from flask import current_app

from alembic import context

# Get Alembic Config object
config = context.config

# Interpret the config file for Python logging
fileConfig(config.config_file_)
logger = logging.getLogger("alembic.env")

# Import the models' MetaData object
# for 'autogenerate' support
from myapp import mymodel
target_metadata = mymodel.Base.metadata

# Other config values can be accessed
# my_important_option = config.get_main_option("my_important_option")

def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, so no DBAPI is required.
    Calls to context.execute() here emit the given
    string to the script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    def process_revision_directives(context, revision, directives):
        if getattr(config.cmd_opts, "autogenerate", False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info("No changes in schema detected.")

    connectable = current_app.extensions["migrate"].db.get_engine()

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_revision_directives=process_revision_directives,
            **current_app.extensions
