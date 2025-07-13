from fastapi import FastAPI
from app.routers import session, chat, payment

app = FastAPI(title="AI Kiosk Server")

# Set Routers
app.include_router(session.router, prefix="/session", tags=["Session"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(payment.router, prefix="/payment", tags=["Payment"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# Run: uvicorn app.main:app --reload
