from fastapi import APIRouter
from app.models.item import Item
from app.services.logic import process_item

router = APIRouter()


@router.get("/hello")
def hello():
    return {"message": "Hello from structured app!"}


@router.post("/items")
def create_item(item: Item):
    result = process_item(item)
    return result
