#Firts off, For working with FastAPI we must create a virtual environment and import it

from typing import Union
from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users
from fastapi.staticfiles import StaticFiles




app = FastAPI()
 # upload the page
# raw python
# Hello FastAPI
# To begin with, We're going to create a function so-called it "root" and it must be async in oder to work well

#Routes 
app.include_router(products.router) # router inclution coming from products
app.include_router(users.router) # router inclution coming from products
app.include_router(basic_auth_users.router) # router inclution coming from basic_auth_user
app.include_router(jwt_auth_users.router) # router inclution coming from jwt_auth_user
app.mount("/static",StaticFiles(directory="static"), name="static") # This is the way to manage static resources like documents, files, pdg, images ans son on, We must import the module "from fastapi.staticfiles import StaticFiles" in order for doing this possible



@app.get("/") # get name "/"
async def  root():
    return "Hi, FastApi"

@app.get("/url") # get name "/url"
async def  url():
    return {"course url":"http//mouredev.com/python"}

#PS C:\Users\ferna\Desktop\backend_24\FastAPI> uvicorn main:app --reload to run our app
#to call each element into Fast PI we must call it for its "get name"
#highlight   http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc, which are useful to document your app from your browser 

# There are many app to make test about the HTTP petitions coming from FastApi, We're going to use a extension coming from "VS code" so-called Thunder Client, Where We make all our requests







