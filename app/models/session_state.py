from datetime import datetime

class SessionState:
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.history = []
        self.intent = None
        self.is_paid = False
        self.created_at = datetime.now()
