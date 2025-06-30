from fastapi import APIRouter
from fastapi.responses import RedirectResponse
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

@router.get("/auth/notion/login")
async def notion_login():
    client_id = os.getenv("NOTION_CLIENT_ID")
    redirect_uri = os.getenv("NOTION_REDIRECT_URI")

    return RedirectResponse(
        f"https://api.notion.com/v1/oauth/authorize?owner=user&client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
    )

@router.get("/auth/notion/callback")
async def notion_callback(code: str):
    return {"message": "✅ Notion OAuth success", "code": code}
