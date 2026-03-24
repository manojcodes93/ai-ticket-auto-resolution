import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key = os.getenv("GROQ_API_KEY")
)

def generate_response(ticket, solutions, category):
    solutions_text = "\n".join([f"- {s}" for s in solutions])

    prompt = f"""
You are a professional IT Support Engineer specializing in enterprise IT systems.

Ticket Category:
{category}

User Issue:
{ticket}

Retrieved Similar Solutions:
{solutions_text}

Your Task:
Generate a concise and actionable resolution for the user's issue.

Guidelines:
- Use the retrieved solutions as context, but do NOT copy them verbatim
- Provide clear technical instructions
- Use step‑by‑step guidance if applicable
- Keep the response concise (2–3 sentences)
- Assume the issue is not yet resolved
- Avoid greetings, filler text, or unnecessary explanations
- Focus on practical resolution steps

Final Resolution:
"""
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role":"user",
                    "content":prompt,
                }
            ],
            model = "llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content

    except Exception as e:
        print("GROQ ERROR:", e)
        return solutions[0]