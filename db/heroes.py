import sqlalchemy
from .base import metadata


heroes = sqlalchemy.Table(
    'heroes',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('name', sqlalchemy.String), 
    sqlalchemy.Column('class_', sqlalchemy.String),
)
