import json
from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


SYSTEM_PROMPT = """
You are a data analyst.

Reply ONLY with a valid JSON object.

The JSON must always have exactly these keys:

{
  "answer": ...,
  "log_url": "PLACEHOLDER"
}

Do not write markdown.
Do not explain.
Return only JSON.
"""


def ask_gemini(question: str) -> dict:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"{SYSTEM_PROMPT}\n\nUser:\n{question}"
    )

    text = response.text.strip()

    try:
        return json.loads(text)
    except Exception:
        return {
            "answer": text,
            "log_url": "PLACEHOLDER"
        }
