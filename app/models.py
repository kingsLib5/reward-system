from pydantic import BaseModel, EmailStr
from pymongo import MongoClient
from bson import ObjectId
from typing import List, Optional
import random
import string

client = MongoClient("mongodb://localhost:27017/")
db = client["reward_system"]

class User(BaseModel):
    email: EmailStr
    referral_code: str
    referred_by: Optional[str] = None
    tasks_completed: List[str] = []
    rewards: List[str] = []

class Task(BaseModel):
    task_name: str
    reward: str

class Reward(BaseModel):
    user_id: str
    task_id: str
    reward_details: str

# Helper function to generate referral code
def generate_referral_code(length: int = 6) -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
