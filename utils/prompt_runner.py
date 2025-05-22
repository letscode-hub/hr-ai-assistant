# utils/prompt_runner.py

from utils.google_client import call_gemini

def call_llm(prompt: str):
    return call_gemini(prompt)
