from pydantic import BaseModel

class JobRequest(BaseModel):
    keyword: str
    location: Optional[str] = "remote"
