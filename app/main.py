from fastapi import FastAPI, File, Form, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from resume_screening.prompts import generate_resume_prompt
from resume_screening.resume_parser import extract_text_from_pdf
from sentiment_analysis.prompts import generate_sentiment_prompt
from sentiment_analysis.feedback_parser import clean_feedback_text
from utils.prompt_runner import call_llm
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/resume-screen", response_class=HTMLResponse)
async def resume_screen(
    request: Request,
    resume: UploadFile = File(...),
    job_desc: str = Form(...)
):
    try:
        ext = resume.filename.split(".")[-1].lower()
        content = await resume.read()

        if ext == "pdf":
            with open("temp_resume.pdf", "wb") as f:
                f.write(content)
            resume_text = extract_text_from_pdf("temp_resume.pdf")
        else:
            resume_text = content.decode("utf-8")

        prompt = generate_resume_prompt(resume_text, job_desc)
        result = call_llm(prompt)

        return templates.TemplateResponse("result.html", {
            "request": request,
            "title": "Resume Screening",
            "result": result
        })

    except Exception as e:
        return HTMLResponse(
            content=f"<h3>❌ Internal Server Error</h3><pre>{str(e)}</pre>",
            status_code=500
        )


@app.post("/sentiment-analyze", response_class=HTMLResponse)
async def sentiment_analyze(request: Request, feedback: UploadFile = File(...)):
    try:
        print("[INFO] Sentiment route hit")
        content = await feedback.read()

        print("[INFO] Feedback uploaded:", feedback.filename)
        feedback_text = clean_feedback_text(content.decode("utf-8"))

        print("[INFO] Cleaned text sample:", feedback_text[:100])
        prompt = generate_sentiment_prompt(feedback_text)

        print("[INFO] Prompt generated")
        result = call_llm(prompt)

        print("[INFO] LLM response received")
        return templates.TemplateResponse("result.html", {
            "request": request,
            "title": "Sentiment Analysis",
            "result": result
        })

    except Exception as e:
        print("[ERROR]", str(e))
        return HTMLResponse(
            content=f"<h3>❌ Internal Server Error</h3><pre>{str(e)}</pre>",
            status_code=500
        )

