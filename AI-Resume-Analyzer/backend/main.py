from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware

from pdf_reader import extract_text_from_pdf
from resume_parser import parse_resume
from job_parser import parse_job_description
from matching_engine import analyze_match
from recommendation_engine import generate_recommendations

app = FastAPI(
    title="AI Resume Analyzer",
    description="AI-powered resume and job matching system",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "AI Resume Analyzer is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    file_path = f"temp_{resume.filename}"

    contents = await resume.read()

    with open(file_path, "wb") as f:
        f.write(contents)

    resume_text = extract_text_from_pdf(file_path)
    parsed_resume = parse_resume(resume_text)
    parsed_job = parse_job_description(job_description)

    analysis = analyze_match(
        resume_text,
        job_description,
        parsed_resume["skills"],
        parsed_job["required_skills"],
        parsed_job["preferred_skills"]
    )

    recommendations = generate_recommendations(
        analysis["missing_required"]
        + analysis["missing_preferred"]
    )

    return {
        "resume": parsed_resume,
        "job": parsed_job,
        "analysis": analysis,
        "recommendations": recommendations
    }
