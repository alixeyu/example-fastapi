from typing import List

from fastapi import APIRouter

from db.base import database
from db.heroes import heroes
from heroes.models import Hero, HeroIn


router = APIRouter()


@router.get('/', response_model=List[Hero])
async def get_all():
    query = heroes.select()
    return await database.fetch_all(query=query)


@router.post('/', response_model=Hero)
async def create_hero(hero: HeroIn):
    query = heroes.insert().values(name=hero.name, class_=hero.class_)
    hero_id = await database.execute(query=query)
    return {**hero.dict(), 'id': hero_id}

@router.put('/', response_model=Hero)
async def update_hero(hero: HeroIn, id: int):
    query = heroes.update().where(heroes.c.id==id).values(name=hero.name, class_=hero.class_)
    hero_id = await database.execute(query=query)
    return {**hero.dict(), 'id': hero_id}


@router.delete('/')
async def delete_hero(id: int):
    query = heroes.delete().where(heroes.c.id==id)
    return await database.execute(query=query)
