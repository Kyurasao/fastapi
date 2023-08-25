from typing import Union, Annotated

import uvicorn
from fastapi import FastAPI, Path, Body, Query
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


@app.put("/items_1/{item_id}")
async def update_item(
        *,
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
        q: Union[str, None] = None,
        w: Annotated[int, Query(gt=1)],
        item: Union[Item, None] = None,
        user: User,
        importance: Annotated[int, Body(gt=4)]
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q, "w": w})
        # if item:
        results.update({"item": item, "user": user, "importance": importance})
    return results


@app.put("/items_2/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
