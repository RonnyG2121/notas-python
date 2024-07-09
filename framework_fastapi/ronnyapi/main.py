from fastapi import FastAPI
from typing import Union

api = FastAPI()

@api.get("/")
def home():
    return "Hola API"


@api.get("/items/{item_id}")
def item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
