from fastapi import FastAPI

from app.db import database
from app.home.routers import router as home_router
from app.items.routers import router as items_router

app = FastAPI()
app.include_router(home_router)
app.include_router(items_router)


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()
