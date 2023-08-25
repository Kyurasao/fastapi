from typing import Union, Annotated

import uvicorn
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items_1/{item_id}")
async def read_items(
        item_id: Annotated[int, Path(title="The ID of the item to get")],
        q: Annotated[Union[str, None], Query(alias="item-query")] = "None",
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_2/{item_id}")
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get")):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_3/{item_id}")
async def read_items(
        q: str, item_id: Annotated[int, Path(title="The ID of the item to get")]
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items_4/{item_id}")
async def read_items(
    item_id: Annotated[float, Path(title="The ID of the item to get", ge=1, le=10)],
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
