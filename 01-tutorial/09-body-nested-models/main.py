from typing import Union, Annotated

import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url_1: str
    url_2: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags_1: list = []
    tags_2: set[str] = set()
    image: Union[list[Image], None] = None


class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: list[Item]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items_1/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


@app.put("/items_2/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    for image in images:
        image.url_1 += "_@"
    return images


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
