import os
from dotenv import load_dotenv
from openai import OpenAI

from logger import logger

load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORG_ID")
)

def detect_intent(text: str) -> str:
    # TODO: call LLM1 and return intent

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """
                AI Kiosk Server의 1차 모듈 역할이야.
                사용자의 질문을 아래 3가지 중 하나로 분류해서 답해.
                해당하지 않으면 "보류"라고 답해.
                ['결제'|'운영'|'메뉴']
                """},
            {"role": "user", "content": text}
        ],
        temperature=0.3
    )

    result = response["choices"][0]["text"]
    logger.info(f"1st LLM result: {result}")

    return result
