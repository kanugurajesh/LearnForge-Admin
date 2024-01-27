from pymongo import MongoClient
from dotenv import load_dotenv
import json
import os

load_dotenv()

api_key = os.getenv("MONGODB_URI")

client = MongoClient(api_key)

db = client['Questions']
collection = db['test']

with open('Anger.json') as f:
    file_data = json.load(f)
    
result = collection.insert_many(file_data)

print('Multiple posts: {0}'.format(result.inserted_ids))