from logging.config import fileConfig
from models import *
from sqlmodel import SQLModel

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
import os, sys
from os.path import join, dirname
from dotenv import load_dotenv


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

POSTGRES_USERNAME = os.environ.get("POSTGRES_USERNAME")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOSTNAME = os.environ.get("POSTGRES_HOSTNAME", "127.0.0.1")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 5432)
POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE", "")
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOSTNAME}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"

config.set_main_option('sqlalchemy.url', SQLALCHEMY_DATABASE_URL)
# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# target_metadata = None
target_metadata = SQLModel.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
