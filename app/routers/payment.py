from fastapi import APIRouter

router = APIRouter()

@router.post("/process")
def process_payment(session_id: str):
    # TODO: implement payment processing logic
    return {"message": "Payment processed"}
