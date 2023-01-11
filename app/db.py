import databases
import sqlalchemy

from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///./base.sqlite3'
database = databases.Database(url=DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(url=DATABASE_URL, connect_args={'check_same_thread': False})
metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
