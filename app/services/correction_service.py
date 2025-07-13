import os
from dotenv import load_dotenv
from openai import OpenAI

from logger import logger

load_dotenv()
client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
    organization=os.getenv("OPENAI_ORG_ID")
)

def correct(text: str) -> str:
    # TODO: implement STT correction logic

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """
                    다음 STT 텍스트를 자연스럽고 올바른 문장으로 고친다.
                    의미를 바꾸지 말고, 문법·맞춤법을 바로잡는다.
                    수정된 텍스트만 출력한다.
                    """},
            {"role": "user", "content": text}
        ],
        temperature=0.3
    )

    result = response.choices[0].message.content.strip()
    logger.info(f"Correction: {text} -> {result}")

    return result
