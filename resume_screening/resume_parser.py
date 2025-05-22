import pdfplumber
import os

def extract_text_from_pdf(pdf_path: str) -> str:
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"File not found: {pdf_path}")

    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        cleaned = text.strip()
        if not cleaned:
            raise ValueError("No extractable text found in PDF.")
        return cleaned
    except Exception as e:
        raise RuntimeError(f"Error parsing PDF '{pdf_path}': {e}")
