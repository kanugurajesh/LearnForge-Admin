import google.generativeai as genai
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os

# loading the .env file
load_dotenv()

# getting the api key from the .env file
api_key = os.getenv("MONGODB_URI")

google_api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=google_api_key)

model = genai.GenerativeModel('gemini-pro')

# passing the api key to the MongoClient constructor
client = MongoClient(api_key)

# Database name is Icons
db = client['Icons']
collection = db['icons']

# get the parent directory of the current directory
directory = os.path.dirname(os.getcwd()) + "/public/courses"

# change the directory to the directory of the courses
os.chdir(directory)

class Item(BaseModel):
    fileUrl: str
    fileName: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload/")
async def create_item(item: Item, status_code: int = 201):
    result = collection.insert_one(item.dict())
    with open('AzureCloud.json', 'r') as file:
        readData = file.read()
        file.close()
    with open(item.fileName + '.json', 'w') as file:
        prompt = prompt = f"change the questions with new questions related to {item.fileName} in the beside data and give me the output in json format => {readData}"
        response = model.generate_content(prompt)
        data = response.text
        # remove the first line of the data
        data = data.split("\n", 1)[1]
        # remove the last line of the data
        data = data.rsplit("\n", 1)[0]
        file.write(data)
        file.close()
    response_content = {"message": "Item created successfully", "item": item.dict()}
    return JSONResponse(content=response_content, status_code=status_code)