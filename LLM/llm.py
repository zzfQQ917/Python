import requests
from dotenv import load_dotenv
import os

load_dotenv()

def llm_answer(query):
    headers = {
        "Authorization": f"Bearer {os.getenv('TOKEN')}",
        "Content-Type": "application/json",
    }
    model_resp = requests.get(os.getenv('URL'), headers=headers, timeout=10)

    model_data = model_resp.json().get("data", [])
    if not model_data:
        raise Exception("No model available on Server LLM")

    model_id = model_data[0]["id"]

    payload = {
        "model": model_id,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": query},
        ],
        "temperature": 0.7,
        "max_tokens": 1024,
    }
    response = requests.post(
        "https://manager.knpu.re.kr/api/llm/v1/chat/completions",
        json=payload,
        headers=headers,
        timeout=60,
    )

    result = response.json()
    return result["choices"][0]["message"]["content"]
