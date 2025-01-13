from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {}

@app.post("/items/")
def create_item(item_id: int, name: str):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = name
    return {"message": "Item created", "item": {item_id: name}}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": {item_id: items[item_id]}}

@app.put("/items/{item_id}")
def update_item(item_id: int, name: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = name
    return {"message": "Item updated", "item": {item_id: name}}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted"}
