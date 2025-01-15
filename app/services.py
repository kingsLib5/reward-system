from .models import Task, Reward
from .email import send_email_notification

def reward_user(user, task):
    reward = Reward(user_id=user["_id"], task_id=task["_id"], reward_details=f"Completed {task['task_name']} task and earned {task['reward']}")
    db.rewards.insert_one(reward.dict())
    
    user["rewards"].append(reward.reward_details)
    db.users.update_one({"_id": user["_id"]}, {"$set": user})
    return reward

def get_user_tasks(user_id):
    user = db.users.find_one({"_id": user_id})
    tasks = db.tasks.find({"_id": {"$nin": user["tasks_completed"]}})
    return list(tasks)

def assign_task_to_user(user_id, task_id):
    task = db.tasks.find_one({"_id": task_id})
    db.users.update_one({"_id": user_id}, {"$push": {"tasks_completed": task_id}})
