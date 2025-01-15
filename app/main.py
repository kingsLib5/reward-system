from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .models import User, Task, Reward, generate_referral_code
from .schemas import UserCreate, TaskComplete
from .services import reward_user, get_user_tasks, assign_task_to_user
from .email import send_email_notification

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Reward System API!"}

@app.post("/signup")
async def signup(user_create: UserCreate):
    referral_code = generate_referral_code()
    user_data = User(email=user_create.email, referral_code=referral_code)
    db.users.insert_one(user_data.dict())

    # Handle referral logic
    # If there is a referral code, the user will be rewarded and notified
    return {"email": user_create.email, "referral_code": referral_code}

@app.post("/complete-task")
async def complete_task(task_complete: TaskComplete):
    user = db.users.find_one({"_id": task_complete.user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    task = db.tasks.find_one({"_id": task_complete.task_id})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    # Add completed task to user's list
    user["tasks_completed"].append(task_complete.task_id)
    db.users.update_one({"_id": task_complete.user_id}, {"$set": user})

    # Reward the user
    reward = reward_user(user, task)
    send_email_notification(user["email"], "Task Completed", f"Reward: {reward['reward_details']}")
    return JSONResponse(content=reward)

@app.get("/tasks/{user_id}")
async def get_tasks(user_id: str):
    tasks = get_user_tasks(user_id)
    return {"tasks": tasks}
