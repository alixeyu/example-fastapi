from sqlalchemy.orm import Session

from . import models, schemas


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item(db: Session, item_id: int) -> models.Item | None:
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(offset=skip).limit(limit=limit).all()


def update_item(db: Session, item: schemas.Item, updates: schemas.ItemUpdate):
    udpated_data = updates.dict(exclude_unset=True)

    for field, value in udpated_data.items():
        setattr(item, field, value)

    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item_id: int) -> int:
    deleted = db.query(models.Item).filter(models.Item.id == item_id).delete()
    db.commit()
    return deleted
