from fastapi import FastAPI

from db.base import init_base
from endpoints import heroes


app = FastAPI()
app.include_router(heroes.router, prefix='/heroes', tags=['heroes'])

init_base()


@app.get('/')
async def root():
    return {'message': 'Hello, world!'}


if __name__ == '__main__':
    app.run()
