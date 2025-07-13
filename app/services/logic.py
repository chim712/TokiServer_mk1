from app.models.item import Item

def process_item(item: Item) -> dict:
    total = item.price * item.quantity
    return {
        "item": item.dict(),
        "total_price": total
    }
