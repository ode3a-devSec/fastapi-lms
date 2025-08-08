from fastapi import FastAPI

app = FastAPI()


# path parameters wit types


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
