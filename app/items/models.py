from sqlalchemy import Column, Integer, String, Boolean

from db import BaseDatabaseClass


class Item(BaseDatabaseClass):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    kind = Column(String)
    rarity = Column(String)
    attunement = Column(Boolean, default=False)
    min_price = Column(Integer)
    max_price = Column(Integer)
    currency = Column(String)
