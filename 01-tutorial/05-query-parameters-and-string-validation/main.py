from typing import Union, Annotated, List

import uvicorn
from fastapi import FastAPI, Query
from pydantic.v1 import Required

app = FastAPI()


@app.get("/items_1/")
async def read_items(q: Annotated[Union[str, None], Query(min_length=3, max_length=50, pattern="^fixedquery$")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_2/")
# Having a default value of any type, including None, makes the parameter optional (not required)!!
async def read_items(q: Annotated[Union[str, None], Query(max_length=50)] = "fixedquery"):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_3/")
async def read_items(q: Annotated[str, Query(min_length=3)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_4/")
async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_5/")
async def read_items(q: Annotated[Union[str, None], Query(min_length=3)] = ...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    # if q:
    #     results.update({"q": q})
    results.update({"q": q})
    return results


@app.get("/items_6/")
async def read_items(q: Annotated[str, Query(min_length=3)] = Required):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_7/")
# можно использовать list[int] или просто list вместо List[str]
async def read_items(q: Annotated[Union[List[str], None], Query()] = None):
    query_items = {"q": q}
    return query_items


@app.get("/items_8/")
# Annotated[List[str], Query()]
async def read_items(q: Annotated[Union[List[str], None], Query()] = None):
    # так будет более правильно, чем ставить заполненные структуры данных в инициализацию функции, чем
    # async def read_items(q: Annotated[Union[List[str], None], Query()] = ["foo", "bar"]):
    # только q я не могу сделать None
    if q is None:
        q = ["foo", "bar"]
    query_items = {"q": q}
    return query_items


@app.get("/items_9/")
async def read_items(q: Annotated[Union[List[str], None], Query()] = ...):
    if q is None:
        q = ["foo", "bar"]
    query_items = {"q": q}
    return query_items


@app.get("/items_10/")
async def read_items(q: Annotated[list, Query()] = []):
    query_items = {"q": q}
    return query_items


@app.get("/items_11/")
# отображается в справке
async def read_items(
    q: Annotated[
        Union[str, None],
        Query(
            title="QuerY StrinG",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        ),
    ] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_12/")
# псевдоним отображается в справке
async def read_items(q: Annotated[Union[str, None], Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo_12"}, {"item_id": "Bar_12"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_13/")
async def read_items(
    q: Annotated[
        Union[str, None],
        Query(
            alias="item-query",
            title="Query strinG",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
