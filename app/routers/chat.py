from fastapi import APIRouter
from app.services import correction_service, llm1_service, llm2_service, payment_service
from app.store.memory_store import get_session
from logger import logger

router = APIRouter()

@router.post("/")
def chat(session_id: str, message: str):
    session = get_session(session_id)

    corrected = correction_service.correct(message)
    intent = llm1_service.detect_intent(corrected)

    if intent == "결제":
        logger.info("payment API call")
        return payment_service.start_payment(session_id)
    if intent == "반려":
        logger.info("ignore strange question")
        return {"response": "매장과 관련된 질문만 부탁드립니다."}
    if intent == "종료":
        logger.info("ignore strange question")
        return {"response": "CloseChat"}

    logger.info("call LLM2 - Intent: " + intent)
    response = llm2_service.generate_response(session.history, corrected, intent)

    session.history.append({"role": "user", "content": corrected})
    session.history.append({"role": "assistant", "content": response})

    return {"response": response}
