from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import SessionLocal
from .models import Item

router = APIRouter(prefix='/items')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/{item_id}', response_model=Item)
def read_item(item_id: int, q: str | None = None):
    return {'item_id': item_id, 'q': q}


@router.get('/', response_model=List[Item])
async def read_items(skip: int, limit: int, db: Session = Depends(get_db)):
    return db.query(Item).offset(skip).limit(limit).all()
