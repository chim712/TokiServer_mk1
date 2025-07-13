import os
from dotenv import load_dotenv
from openai import OpenAI

from logger import logger

load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORG_ID")
)

def generate_response(history, text: str, intent: str) -> str:
    # TODO: call LLM2 and return generated response

    if intent == "운영":
        prompt = """
        당신은 김밥스크립트 매장의 AI 키오스크입니다.
        고객님의 질문에 친절하고 정중한 존댓말로 답변해 주세요.
        매장 운영에 관한 질문에 학습 내용을 기반으로 답변하세요.
        """

    elif intent == "메뉴":
        prompt = """
        당신은 김밥스크립트 매장의 AI 키오스크입니다.
        고객님의 질문에 친절하고 정중한 존댓말로 답변해 주세요.
        판매 음식(메뉴)에 관한 질문에 학습 내용을 기반으로 답변하세요.
        """
    else:
        return "Error"

    msg = history.append({"role": "system", "content": prompt}).append({"role": "user", "content": text})
    #-------------------
    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-1106:personal:ai-kiosk-mk2:BqRCg1BJ",
        messages=msg,
        temperature=0.8
    )

    result = response.choices[0].message.content.strip()
    logger.info(f"2nd LLM result: {result}")

    return result

