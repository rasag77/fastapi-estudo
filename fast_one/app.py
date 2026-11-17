from http import HTTPStatus

from fastapi import FastAPI

from fast_one.schemas import Message

app = FastAPI(title='Rubens no fastapi')


@app.get('/',
status_code=HTTPStatus.OK,
response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
