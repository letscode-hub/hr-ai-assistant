def generate_sentiment_prompt(feedback_text: str) -> str:
    return f"""
You are an HR sentiment analyst. Analyze the following employee feedback and return insights in JSON format.

Tasks:
- Classify sentiment as one of: Positive, Neutral, or Negative
- Identify key concerns (e.g., Workload, Compensation, Management, Growth)
- Predict attrition risk: Yes or No
- Suggest one engagement strategy to retain this employee

Feedback:
\"\"\"
{feedback_text}
\"\"\"

Respond strictly in this JSON format:
{{
  "sentiment": "...",
  "key_issues": [...],
  "attrition_risk": "...",
  "recommendation": "..."
}}
"""
