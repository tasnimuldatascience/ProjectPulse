import os
from dotenv import load_dotenv
import openai

load_dotenv()

# Initialize OpenAI client (compatible with openai>=1.0.0)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_cover_letter(job_title: str, company: str, resume_snippet: str = "") -> str:
    """
    Generates a personalized cover letter for the given job and company.
    Optionally includes resume_snippet extracted from uploaded resume.
    """
    # Fallback: import resume_text from global if not passed directly
    if not resume_snippet:
        try:
            from app.routes.job import resume_text
            resume_snippet = resume_text or ""
        except ImportError:
            resume_snippet = ""

    # Limit resume to first 1500 characters to avoid long tokens
    resume_text_cleaned = resume_snippet.strip().replace("\n", " ")[:1500]

    # Prompt sent to GPT-4
    prompt = f"""
    Write a professional and friendly cover letter for the position of '{job_title}' at '{company}'.
    Tailor the tone to emphasize adaptability, curiosity, and problem-solving.

    The applicant's resume is summarized below:

    {resume_text_cleaned}

    The letter should:
    - Be addressed to the hiring manager
    - Be 3-5 paragraphs
    - Highlight relevant skills and experience
    - Show enthusiasm for the company

    Return only the letter body (no subject or headers).
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=600
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"❌ Error generating cover letter: {e}")
        return "Error: Could not generate cover letter."
