from typing import Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    description: Optional[str] = None
    content: str