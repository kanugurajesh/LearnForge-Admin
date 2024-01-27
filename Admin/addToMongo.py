from pymongo import MongoClient
from dotenv import load_dotenv
import json
import os

# loading the .env file
load_dotenv()

# getting the api key from the .env file
api_key = os.getenv("MONGODB_URI")

# passing the api key to the MongoClient constructor
client = MongoClient(api_key)

# Database name is Questions
db = client['Questions']
    
# get all the files in the course directory
files = os.listdir('./courses')

# iterate through all the files and add them to the database
for i in files:
    with open(f"./courses/{i}") as f:
        # loading the json data
        file_data = json.load(f)
        # clear the collection before adding new data
        db[i.split('.')[0]].delete_many({})
        # creating a new collection
        collection = db[i.split('.')[0]]
        # adding the data to the collection
        result = collection.insert_many(file_data)