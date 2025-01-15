from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    email: str

class TaskComplete(BaseModel):
    task_id: str
    user_id: str
