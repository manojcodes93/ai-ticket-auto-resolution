import requests
import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(Path(__file__).resolve().parents[1] / ".env")
HF_TOKEN = os.getenv("HF_TOKEN")
print(HF_TOKEN)

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

def generate_response(ticket, solutions):
    solutions_text = "\n".join([f"- {s}" for s in solutions])

    prompt = f"""
You are an IT support assistant.

User issue:
{ticket}

Possible solutions:
{solutions_text}

Give a short and clear solution (2-3 sentences).
"""

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt},
            timeout=10
        )

        print(response.status_code)
        print(response.text)

        result = response.json()

        # Handle HF errors
        if isinstance(result, dict) and "error" in result:
            print("HF ERROR:", result)
            return solutions[0]

        # Extract response properly
        if isinstance(result, list):
            return result[0].get("generated_text", solutions[0])

        return solutions[0]

    except Exception as e:
        print("Exception:", e)
        return solutions[0]