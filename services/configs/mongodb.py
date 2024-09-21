import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


client = MongoClient(
    host=os.environ.get("MONGO_HOST", "localhost"),
    port=int(os.environ.get("MONGO_PORT", 27017)),
)

database = client[os.environ.get("MONGO_DB", "todo_app")]
