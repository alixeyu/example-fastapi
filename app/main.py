from fastapi import FastAPI

from app.home.routers import router as home_router

app = FastAPI()
app.include_router(home_router)
