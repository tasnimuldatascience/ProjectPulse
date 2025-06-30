from fastapi import APIRouter
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

@router.get("/auth/google/login")
async def google_login():
    client_id = os.getenv("GOOGLE_CLIENT_ID")
    redirect_uri = os.getenv("GOOGLE_REDIRECT_URI")
    scope = "https://www.googleapis.com/auth/documents"

    return RedirectResponse(
        f"https://accounts.google.com/o/oauth2/v2/auth?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope={scope}&access_type=offline&prompt=consent"
    )

@router.get("/auth/google/callback")
async def google_callback(code: str):
    return {"message": "✅ Google OAuth success", "code": code}
