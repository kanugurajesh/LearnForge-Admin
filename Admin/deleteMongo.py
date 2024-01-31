from pymongo import MongoClient
from dotenv import load_dotenv
import os

# loading the .env file
load_dotenv()

# getting the api key from the .env file
api_key = os.getenv("MONGODB_URI")

# passing the api key to the MongoClient constructor
client = MongoClient(api_key)

# Database name is Questions
db = client['Questions']

# Get the list of collections in the database
collections = db.list_collection_names()

# Delete each collection
for collection_name in collections:
    db[collection_name].drop()

# Optionally, you can print a message after deleting all collections
print("All collections in the database have been deleted.")
