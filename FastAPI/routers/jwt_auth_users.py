
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError #jwt json web token 
from passlib.context import CryptContext
from datetime import datetime, timedelta # this module going to be woorking with dates and making easy calculate differents amidts dates

# JWT (JSON Web Token) authentication is a standard for creating access tokens that enable secure authentication and transmission of information between parties. JWT is a token format that contains encoded information in JSON format and is commonly used in authenticating web routerlications and APIs.
# Moreover We need to install a libraries passlib and python_jose for manage the criptografy 


router = APIRouter()

crypt = CryptContext(schemes=["bcrypt"]) # This variable is for working on encrypt algorithms https://bcrypt-generator.com/

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") # These modules are for authenticating the user. The first module handles both user and password data, and the second one defines how to send data and how our backend handles it.

ALGORITHM = "HS256" # this is an algorithm which is used for working on cryptography, In addition, It´s the most used algorithm. # https://jwt.io/

ACESS_TOKEN_DURATION = 1

SECRET = "b35e63ba9beb97f194d9b1fe4f1e832dc3c4e7f8b2b0a0fa1e07093cfb00aff7" #this code coming from "openssl rand -hex 32" and for running this you must run it on bash to get this kind of code


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
        "password": "$2a$12$77V2MbYndTn7V04MUi6FKeHT48MDz/ke35i9kWK5DpFYQCkv3Ffqm" # encrypt password
    },
    "fersh": {
        "username": "fersh", # Removed the extra comma
        "full_name": "Fernando Calvillo",
        "email": "fsanagustini10@gmail.com", # Corrected email
        "disabled": True, # Corrected to 'disabled'
        "password": "$2a$12$Sz/Ap5uVIgvaMUd6OZH0reEOD39tApFFXg2iB/hg/q8ou3LSqZrle" # encrypt password
    }
}

def search_user(username: str): # This function checks if the user exists or not
    if username in users_db:
        return User(**users_db[username])

def search_user_db(username: str): # This function checks if the user exists or not but it's a data base user, it means if we call it the display shoecases the password as well.
    if username in users_db:
        return UserDB(**users_db[username])
    

    
async def auth_user(token: str = Depends(oauth2_scheme)):

    exception =  HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"}
        )
    
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except JWTError:
         raise exception
    
    return search_user(username)

    
async def current_user(user: User = Depends(auth_user)): # This function authenticates the user
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactived user "
        )
    
    return user
    

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):

    user_db = users_db.get(form_data.username)

    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username"
        )
    
    user = search_user_db(form_data.username)

    if not crypt.verify(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )

    access_token ={
                    "sub": user.username,
                    "exp":datetime.utcnow() +  timedelta(minutes=ACESS_TOKEN_DURATION)
                    # "exp" is an abbreviation for expire
                    } 

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}
    
@router.get("/user/me")
async def read_users_me(user: User = Depends(current_user)): # This endpoint returns the current user information
    return user

