import databases
import sqlalchemy

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./base.sqlite3"
database = databases.Database(url=DATABASE_URL)
engine = sqlalchemy.create_engine(
    url=DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
BaseDatabaseClass = declarative_base()
