import enum


class ItemKind(str, enum.Enum):
    ROD = 'rod'
    ARMOR = 'armor'
    WAND = 'wand'
    POTION = 'potion'
    RING = 'ring'
    WEAPON = 'weapon'
    STAFF = 'staff'
    SCROLL = 'scroll'
    WONDROUS = 'wondrous item'


class ItemRarity(str, enum.Enum):
    COMMON = 'common'
    UNCOMMON = 'uncommon'
    RARE = 'rare'
    VERY_RARE = 'very rare'
    LEGANDARY = 'legendary'


class ItemCurrency(str, enum.Enum):
    COPPER = 'copper'
    SILVER = 'silver'
    GOLD = 'gold'
    PLATINUM = 'platinum'
    ASTRAL_DIAMOND = 'astral diamond'
