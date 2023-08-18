from fastapi import FastAPI

KEY = {'1': 1, '2': 2, '3': 3}

app = FastAPI()


@app.get("/")
async def root():
    # return {"message": "Hello World!"}
    return KEY
