# database/db_setup.py

from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database.models import Base
from config import DATABASE_URL


# Define your database connection details
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_empty_database():
    session = SessionLocal()
    create_tables_from_models()
    session.commit()

    session.close()


def create_tables_from_models():
    with engine.connect() as conn:
        Base.metadata.create_all(bind=engine)
        conn.commit()


def rewrite_tables_from_models():
    with engine.connect() as conn:
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        conn.commit()
        conn.close()

    print('Tables have been rewritten.')



