import os
from sentiment_analysis.prompts import generate_sentiment_prompt
from sentiment_analysis.feedback_parser import clean_feedback_text
from utils.prompt_runner import call_llm

def run_sentiment_analysis(feedback_path: str) -> str:
    with open(feedback_path, "r", encoding="utf-8") as f:
        feedback_text = f.read()

    cleaned_text = clean_feedback_text(feedback_text)
    prompt = generate_sentiment_prompt(cleaned_text)
    result = call_llm(prompt)

    print("🧠 Sentiment Analysis Result:\n", result)
    return result

if __name__ == "__main__":
    run_sentiment_analysis("sentiment_analysis/examples/feedback_1.txt")
