from fastapi import FastAPI

app = FastAPI()


# path parameters


@app.get("/items/{item_id}")
async def read_time(item_id):
    return {"item_id": item_id}
