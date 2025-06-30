from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from typing import Optional
from PyPDF2 import PdfReader
from docx import Document
import os
from dotenv import load_dotenv

from app.services.job_scraper import scrape_remoteok_jobs
from app.services.notion_service import insert_into_notion
from app.services.google_docs_service import generate_doc
from app.services.cover_letter_service import generate_cover_letter

router = APIRouter()

# Load environment variables
load_dotenv()
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")
GOOGLE_TOKEN = os.getenv("GOOGLE_TOKEN")

# Global variable for storing resume text
resume_text = ""

# 📤 Upload Resume Endpoint (path will be /job/upload-resume)
@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    global resume_text
    if file.filename.endswith(".pdf"):
        reader = PdfReader(file.file)
        resume_text = "".join(page.extract_text() or "" for page in reader.pages)
    elif file.filename.endswith(".docx"):
        doc = Document(file.file)
        resume_text = "\n".join([p.text for p in doc.paragraphs])
    else:
        return {"error": "Unsupported file type"}
    return {"message": "✅ Resume uploaded successfully"}

# 📄 JobRequest model for /job/auto
class JobRequest(BaseModel):
    keyword: str
    location: Optional[str] = "remote"

# 🚀 Main Auto-Pipeline Endpoint (path will be /job/auto)
@router.post("/auto")
async def auto_pipeline(payload: JobRequest):
    keyword = payload.keyword
    jobs = scrape_remoteok_jobs(keyword)

    results = []

    for job in jobs:
        title = job["title"]
        company = job["company"]
        link = job["link"]

        cover_letter = generate_cover_letter(title, company, resume_text)
        job_title = f"{title} at {company}"
        doc_url = generate_doc(cover_letter, GOOGLE_TOKEN, job_title)
        notion_url = insert_into_notion(title, company, link, NOTION_TOKEN, DATABASE_ID)

        results.append({
            "title": title,
            "company": company,
            "job_link": link,
            "cover_letter": cover_letter,
            "google_doc": doc_url,
            "notion_entry": notion_url
        })

    return {"jobs": results}
