import os, sys
from os.path import join, dirname
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# SQLALCHEMY_SQLITE_URL = "sqlite:///./blog.db"
POSTGRES_USERNAME = os.environ.get("POSTGRES_USERNAME")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOSTNAME = os.environ.get("POSTGRES_HOSTNAME", "127.0.0.1")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT", 5432)
POSTGRES_DATABASE = os.environ.get("POSTGRES_DATABASE", "")
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_HOSTNAME}:{POSTGRES_PORT}/{POSTGRES_DATABASE}"

#engine = create_engine(
#    SQLALCHEMY_SQLITE_URL, connect_args={"check_same_thread": False}
#)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
