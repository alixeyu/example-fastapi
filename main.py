from fastapi import FastAPI

from db.base import init_base
from heroes.endpoints import router as heroes_router


app = FastAPI()
app.include_router(heroes_router, prefix='/heroes', tags=['heroes'])

init_base()


@app.get('/')
async def root():
    return {'message': 'Hello, world!'}


if __name__ == '__main__':
    app.run()
