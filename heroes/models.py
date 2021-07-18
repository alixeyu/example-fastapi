from pydantic import BaseModel


class HeroIn(BaseModel):
    name: str
    class_: str


class Hero(BaseModel):
    id: int
    name: str
    class_: str
