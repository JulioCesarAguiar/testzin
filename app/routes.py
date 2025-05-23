from fastapi import APIRouter, HTTPException
from app.models import Item
from app.storage import items

router = APIRouter()

@router.get("/items/")
async def get_items():
    return items

@router.post("/items/")
async def create_item(item: Item):
    for existing_item in items:
        if existing_item["id"] == item.id:
            raise HTTPException(status_code=400, detail="Item já existe")
    items.append(item.model_dump())
    return item

@router.get("/items/{item_id}")
async def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")
