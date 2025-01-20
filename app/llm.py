import requests
import json

from app.settings import HF_API_TOKEN, LLM_MODEL, DEBUG
from app.prompt import prompt


def llm_infer(query: str, context: str) -> dict:
    parameters = {
        "max_new_tokens": 5000,
        "temperature": 0.01,
        "top_k": 50,
        "top_p": 0.95,
        "return_full_text": False,
    }
    url = f"https://api-inference.huggingface.co/models/{LLM_MODEL}"

    headers = {
        "Authorization": f"Bearer {HF_API_TOKEN}",
        "Content-Type": "application/json",
    }

    prompt_filled = prompt.replace("{context}", context).replace("{question}", query)

    payload = {"inputs": prompt_filled, "parameters": parameters}

    if DEBUG:
        print("Quering llm...")

    result = {}
    try:
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()

        if DEBUG:
            print(f"LLM response: {result}")

        result = json.loads(result[0]["generated_text"])
    except Exception:
        pass

    return result
