from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


#As from here, We're going to create an api for users by scratch
## uvicorn users:app --reload for this file we must run it in this direction

#@app.get("/users") 
#async def  users():
#    return "Hi, Users"

# Entity users

class User(BaseModel): # base model is a tool which aids us out to build a class into a easy way
    name: str
    surname: str
    url: str
    age: int

user_list = [User(name = "Ivan",surname ="Calvillo",url = "https://www.facebook.com/ivanfernando.calvillosanagustin/,", age = 30)] # It might be a database

# json manual
@app.get("/usersjson") 
async def  usersjson():
    return {"name":"Ivan","surname": "Calvillo","url": "https://www.facebook.com/ivanfernando.calvillosanagustin/"}

# json from a base model
@app.get("/user_class") 
async def  user_class():
    return user_list
