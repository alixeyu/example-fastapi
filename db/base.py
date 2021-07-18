import databases
import sqlalchemy


DATABASE_URL = 'sqlite:///./base.sqlite3'
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={'check_same_thread': False})


def init_base():
    metadata.create_all(engine)
