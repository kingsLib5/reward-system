from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# MongoDB connection URL from the environment variable
MONGODB_URL = os.getenv("MONGODB_URL")

# Create a client and database connection
client = MongoClient(MONGODB_URL)
db = client.get_database()

# Ensure collections exist
if "users" not in db.list_collection_names():
    db.create_collection("users")

if "tasks" not in db.list_collection_names():
    db.create_collection("tasks")

if "rewards" not in db.list_collection_names():
    db.create_collection("rewards")
