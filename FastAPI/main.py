#Firts off, For working with FastAPI we must create a virtual environment and import it

from typing import Union

from fastapi import FastAPI

app = FastAPI()
 # upload the page
# raw python
# Hello FastAPI
# To begin with, We're going to create a function so-called it "root" and it must be async in oder to work well
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