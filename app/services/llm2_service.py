import os
from dotenv import load_dotenv
from openai import OpenAI

from logger import logger

load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORG_ID")
)

def generate_response(text: str, intent: str) -> str:
    # TODO: call LLM2 and return generated response

    if intent == "운영":
        prompt = " "

    elif intent == "메뉴":
        prompt = " "
    else:
        return "Error"

    #-------------------
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": text}
        ],
        temperature=0.38
    )

    result = response["choices"][0]["text"]
    logger.info(f"2nd LLM result: {result}")

    return result

