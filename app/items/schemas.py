from pydantic import BaseModel

from .enums import ItemCurrency, ItemKind, ItemRarity


class ItemBase(BaseModel):
    name: str
    kind: ItemKind
    rarity: ItemRarity
    attunement: bool = False
    min_price: int
    max_price: int
    currency: ItemCurrency

    @property
    def price(self):
        return (self.min_price, self.max_price, self.currency)


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    name: str = ''
    kind: ItemKind = ItemKind.ROD
    rarity: ItemRarity = ItemRarity.COMMON
    attunement: bool = False
    min_price: int = 0
    max_price: int = 0
    currency: ItemCurrency = ItemCurrency.COPPER


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
