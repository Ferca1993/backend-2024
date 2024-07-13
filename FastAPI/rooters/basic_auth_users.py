from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") # These modules are for authenticating the user. The first module handles both user and password data, and the second one defines how to send data and how our backend handles it.

class User(BaseModel): # BaseModel is a tool that helps us build a class in an easy way
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User): # Inherits from User to avoid redundancy
    password: str

users_db = { # This is a sample of a database
    "ferca": {
        "username": "ferca",
        "full_name": "Ivan Calvillo",
        "email": "Ivan.F.Calvillo@gmail.com", # Corrected email
        "disabled": False, # Corrected to 'disabled'
        "password": "120893"
    },
    "fersh": {
        "username": "fersh", # Removed the extra comma
        "full_name": "Fernando Calvillo",
        "email": "fsanagustini10@gmail.com", # Corrected email
        "disabled": True, # Corrected to 'disabled'
        "password": "081293"
    }
}

def search_user(username: str): # This function checks if the user exists or not
    if username in users_db:
        return User(**users_db[username])
    

def search_user_db(username: str): # This function checks if the user exists or not but it's a data base user, it means if we call it the display shoecases the password as well.
    if username in users_db:
        return UserDB(**users_db[username])

async def current_user(token: str = Depends(oauth2_scheme)): # This function authenticates the user
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactived user "
        )
    
    return user

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form_data.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username"
        )

    user = search_user_db(form_data.username)
    if not user or user.password != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )
    
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/user/me")
async def read_users_me(current_user: User = Depends(current_user)): # This endpoint returns the current user information
    return current_user
