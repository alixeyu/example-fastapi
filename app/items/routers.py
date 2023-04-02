from typing import Generator, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import SessionLocal
from . import crud
from . import models
from . import schemas

router = APIRouter(tags=["items"])


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.put("/items", response_model=schemas.Item)
async def create_item(
    item: schemas.ItemCreate, db: Session = Depends(get_db)
) -> models.Item:
    return crud.create_item(db=db, item=item)


@router.get("/items/{item_id}", response_model=schemas.Item)
async def read_item(item_id: int, db: Session = Depends(get_db)) -> models.Item:
    db_item = crud.get_item(db=db, item_id=item_id)

    if db_item is None:
        raise HTTPException(
            status_code=400, detail=f"Item with id {item_id} not found."
        )

    return db_item


@router.get("/items", response_model=List[schemas.Item])
async def read_items(
    skip: int, limit: int, db: Session = Depends(get_db)
) -> List[models.Item]:
    return crud.get_items(db=db, skip=skip, limit=limit)


@router.patch("/items/{item_id}", response_model=schemas.Item)
async def update_item(
    item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)
) -> models.Item:
    db_item = crud.get_item(db=db, item_id=item_id)

    if db_item is None:
        raise HTTPException(
            status_code=400, detail=f"Item with id {item_id} not found."
        )

    return crud.update_item(db=db, item=db_item, updates=item)


@router.delete("/items/{item_id}")
async def delete_item(item_id: int, db: Session = Depends(get_db)) -> int:
    return crud.delete_item(db=db, item_id=item_id)
