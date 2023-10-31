import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import logging

from src.application import config

Base = declarative_base()
engine = create_engine(config.SQL_ALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker()
SessionLocal.configure(bind=engine)

logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
