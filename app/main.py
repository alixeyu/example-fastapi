from fastapi import FastAPI

from app.db import BaseDatabaseClass, engine
from app.home.routers import router as home_router
from app.items.routers import router as items_router


BaseDatabaseClass.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(home_router)
app.include_router(items_router)
