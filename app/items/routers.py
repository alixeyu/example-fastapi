from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import SessionLocal
from . import crud
from . import schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.put('/items', response_model=schemas.Item)
async def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@router.get('/items/{item_id}', response_model=schemas.Item)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db=db, item_id=item_id)

    if db_item is None:
        raise HTTPException(status_code=400, detail=f'Item with id {item_id} not found.')

    return db_item


@router.get('/items', response_model=List[schemas.Item])
async def read_items(skip: int, limit: int, db: Session = Depends(get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)
