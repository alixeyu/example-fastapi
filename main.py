from fastapi import FastAPI

from db.base import init_base

app = FastAPI()


init_base()


@app.get('/')
async def root():
    return {'message': 'Hello, world!'}


if __name__ == '__main__':
    app.run()
