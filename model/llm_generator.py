import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_response(ticket, solutions):

    solutions_text = "\n".join([f"- {s}" for s in solutions])

    prompt = f"""
You are an IT support assistant.

User ticket:
{ticket}

Possible solutions:
{solutions_text}

Write a SHORT response explaining how the user can fix the issue.

Rules:
- Do NOT assume the issue is already resolved
- Provide clear instructions
- Limit to 2–3 sentences
- Do NOT include greetings like 'Dear user'
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]