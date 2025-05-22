import os
import requests
import re

def call_gemini(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY not found in environment variables.")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        raw_output = response.json()["candidates"][0]["content"]["parts"][0]["text"]

        # Strip code block markdown (e.g., ```json ... ```)
        clean_output = re.sub(r"^```json\n?|```$", "", raw_output.strip(), flags=re.DOTALL)
        return clean_output.strip()

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"API request failed: {e}")
    except (KeyError, IndexError) as e:
        raise RuntimeError(f"Unexpected response structure: {e}")
