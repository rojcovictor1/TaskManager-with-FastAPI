from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskCreate(BaseModel):
    title: str  # Task title
    description: Optional[str] = None  # Optional task description


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    is_completed: bool
    created_at: datetime

    class Config:
        orm_mode = True  # Allows Pydantic to work with ORM objects
