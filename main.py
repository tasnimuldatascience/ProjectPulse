from fastapi import FastAPI
from dotenv import load_dotenv
import os

from app.routes import job
from app.routes.notion_auth import router as notion_router
from app.routes.google_auth import router as google_router

load_dotenv()

app = FastAPI(title="ProjectPulse MCP Server")

app.include_router(job.router, prefix="/job")
app.include_router(notion_router)
app.include_router(google_router)