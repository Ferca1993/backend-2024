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
    id : int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id = 1 ,name = "Ivan",surname ="Calvillo",url = "https://www.facebook.com/ivanfernando.calvillosanagustin/,", age = 30),User(id = 2, name = "Fersh",surname ="San Agustin",url = "https://www.facebook.com/ivanfernando.calvillosanagustin/,", age = 31)] # It might be a database

# json manual
@app.get("/usersjson") 
async def  usersjson():
    return {"name":"Ivan","surname": "Calvillo","url": "https://www.facebook.com/ivanfernando.calvillosanagustin/"}

# json from a base model
@app.get("/users_class") 
async def  users_class():
    return users_list

def search_user(id: int):
    users = filter(lambda user:user.id == id, users_list )
    try:
        return list(users)[0]
    except:
        return "Error, the user weren't found "
        #http://127.0.0.1:8000/user_query/?id=1 user by query


# path model
@app.get("/user/{id}") # In this fucntion is We can give parameters to it, I t means, This case We're gonna seeking out a user by its id
async def  user_id(id: int):
    return search_user(id)
    

# query model
@app.get("/user/") # "Calling a user by their ID means accessing them through bounded data."
async def  user_query(id: int, name: str):
    return search_user(id)


