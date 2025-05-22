import re

def clean_feedback_text(text: str) -> str:
    """
    Cleans raw feedback text by normalizing whitespace and removing non-informative characters.
    """
    # Remove extra newlines and tabs
    text = re.sub(r'[\n\t\r]+', ' ', text)

    # Collapse multiple spaces to a single space
    text = re.sub(r'\s+', ' ', text)

    # Remove leading/trailing whitespace
    return text.strip()
