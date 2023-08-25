from typing import Union, Annotated

import uvicorn
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
        q: Union[str, None] = None,
        item: Union[Item, None] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80)
