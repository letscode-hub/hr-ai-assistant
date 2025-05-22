def generate_resume_prompt(resume_text: str, job_description: str) -> str:
    return f"""
You are a resume screening expert. Extract the following information from the resume below:

- Candidate Name
- Total Years of Experience
- Programming Languages
- Frameworks and Libraries
- Cloud Platforms
- Education Qualifications
- Match Score (0 to 100) for the following job:
{job_description}

Resume:
\"\"\"
{resume_text}
\"\"\"

Return the extracted information in valid JSON format with keys:
name, experience, languages, frameworks, cloud, education, match_score.
"""
