from models.session_state import SessionState
from logger import logger

_sessions = {}

def save_session(session_id: str):
    _sessions[session_id] = SessionState(session_id)
    logger.info(f"Saving session {session_id}")

def get_session(session_id: str) -> SessionState:
    return _sessions.get(session_id)

def update_session(session_id: str, session_state: SessionState):
    _sessions[session_id] = session_state
    logger.info(f"Update session {session_id}")

def end_session(session_id: str):
    _sessions.pop(session_id, None)
    logger.info(f"Delete session {session_id}")
