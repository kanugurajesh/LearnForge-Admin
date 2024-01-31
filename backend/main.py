from typing import Union

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class Item(BaseModel):
    fileUrl: str
    fileName: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload/")
async def create_item(item: Item, status_code: int = 201):
    print(item)
    response_content = {"message": "Item created successfully", "item": item.dict()}
    return JSONResponse(content=response_content, status_code=status_code)
