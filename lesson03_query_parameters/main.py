from fastapi import FastAPI

app = FastAPI()


# http://127.0.0.1:8000/items/20?q=3
# http://127.0.0.1:8000/items/20


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
