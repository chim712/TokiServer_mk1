from fastapi import APIRouter
from app.utils.id_generator import generate_session_id
from app.store.memory_store import save_session, end_session

router = APIRouter()

@router.post("/start")
def start_session():
    session_id = generate_session_id()
    save_session(session_id)
    return {"session_id": session_id}

@router.post("/complete")
def complete_session(session_id: str):
    end_session(session_id)
    return {"message": f"Session {session_id} completed"}
