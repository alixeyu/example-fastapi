import sqlalchemy

from app.db import metadata


items = sqlalchemy.Table(
    "items",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("rarity", sqlalchemy.String),
    sqlalchemy.Column("attunement", sqlalchemy.Boolean),
    sqlalchemy.Column("min_price", sqlalchemy.Integer),
    sqlalchemy.Column("max_price", sqlalchemy.Integer),
    sqlalchemy.Column("currency", sqlalchemy.String),
)
