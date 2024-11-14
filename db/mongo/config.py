import os

from dotenv import load_dotenv
from pymongo import MongoClient
load_dotenv(verbose=True)
client = MongoClient(os.environ["MONGO_URL"])
db = client["email_enemy"]

row_data = db["row_data"]