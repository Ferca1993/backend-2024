from fastapi import APIRouter, HTTPException
router = APIRouter(prefix="/products", 
                   tags=["products"],
                   responses= {404: {"message" : "No found"}} ) #This is a way to set up the path for all functions into a router, moreover, we customize a response in case to throws an error

# Now, As a result of as things go, We're going to create a API for products and knowing the root concept to run various API server at the same time.
#For thaT We'll built in a new folder where We wrap all routes up
#right now, We import APIRouter instead of FastAPI in order for going on with this new feature
#In a routers all path must have same path name

product_list = ["Productos 1","Productos 2","Productos 3","Productos 4","Productos 5"]


@router.get("/") 
async def  products():
    return product_list

@router.get("/{id}") 
async def  products(id: int):
    return product_list[id]
    