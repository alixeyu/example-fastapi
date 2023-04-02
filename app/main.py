from fastapi import FastAPI

from db import BaseDatabaseClass, engine
from home.routers import router as home_router
from items.routers import router as items_router


BaseDatabaseClass.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(home_router)
app.include_router(items_router)
