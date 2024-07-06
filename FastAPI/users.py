from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import *
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
    return {"id": 3, "name":"Ivan","surname": "Calvillo","url": "https://www.facebook.com/ivanfernando.calvillosanagustin/","age": 31}


# json from a base model
@app.get("/users") 
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

# post request 
# This action is to append new data

@app.post("/user/",response_model=User,status_code=201) # The status code is a parameter to specifide a http code rightly (201 = Created The request succeeded, and a new resource was created as a result. This is typically the response sent after POST requests, or some PUT requests. ) 
# The response model is helpful to return or as a return, getting back a outcome when the request has been made correctly.  
async def post_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204,detail="the user already exists") # The HTTPExeption is to make code inside of a functnion and showing a http code bases on a prompt, in addition, HTTPExeptions also can set up with own error in detail parameter
    else: 
        users_list.append(user)
        return user


# when you're import a module you must use the function, class etc in order to watch them visible in the currenct file
 # Into a dictionary, it can't handle floats numbers, they must be integer for working well

#put request is helpful updating data 
#there are many way to update the data, it might be by whole user or by each data of user
#When I make any change in my APP in FastAPI Always the server reset by itself

@app.put("/user/")
async def put_user(user: User):
    found = False
    for index, updated_user in enumerate(users_list):
        if updated_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        return "Error, The user hadn't been updated" 
    else:
        return user



@app.delete("/user/{id}") # Here We reuse "get path model" due to it contains the necessary logic to solve this issue.
async def delete_user(id: int):
    found = False

    for index, updated_user in enumerate(users_list):
        if updated_user.id == id:
            #del users_list[index]
            delete = users_list.pop(index) # my own contribution
            found = True
            return delete
            
    if not found:
        return "Error, The user hadn't been deleted" 
    
# http status code 

# Informational responses (100 – 199)
# Successful responses (200 – 299)
# Redirection messages (300 – 399)
# Client error responses (400 – 499)
# Server error responses (500 – 599)

