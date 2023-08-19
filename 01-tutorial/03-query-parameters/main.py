from enum import Enum
from typing import Union

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class ItemName(str, Enum):
    one = "one"
    two = "two"
    three = "three"


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/items/needy/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item


@app.get("/items_all/{item_id}")
async def read_user_item(
        # num: ItemName,
        item_id: ItemName,
        needy: str,
        skip: int = 0,
        limit: Union[int, None] = None,
):
    item = {
        # "item_id": item_id,
        "needy": needy,
        "skip": skip,
        "limit": limit}
    if item_id.value == "one":
        item.update({"item_id": item_id, "message": "This is one!"})
    else:
        item.update({"item_id": item_id})
    return item
