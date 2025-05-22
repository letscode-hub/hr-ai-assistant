import os
from resume_screening.prompts import generate_resume_prompt
from resume_screening.resume_parser import extract_text_from_pdf
from utils.prompt_runner import call_llm

def read_resume(resume_path: str) -> str:
    if resume_path.endswith(".pdf"):
        return extract_text_from_pdf(resume_path)
    elif resume_path.endswith(".txt"):
        with open(resume_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError("Unsupported file format. Please use .txt or .pdf.")

def run_resume_screening(resume_path: str, jd_path: str) -> str:
    resume_text = read_resume(resume_path)

    with open(jd_path, "r", encoding="utf-8") as f:
        job_description = f.read()

    prompt = generate_resume_prompt(resume_text, job_description)
    result = call_llm(prompt)
    
    print("🎯 Resume Screening Result:\n", result)
    return result

if __name__ == "__main__":
    run_resume_screening(
        "resume_screening/examples/sample_resume_1.txt",  # or .pdf
        "resume_screening/job_description.txt"
    )
