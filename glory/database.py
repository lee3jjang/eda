from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, registry
from starlette.config import Config

config = Config(".env")

SQLALCHEMY_DATABASE_URL = config("SQLALCHEMY_DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: registry = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
