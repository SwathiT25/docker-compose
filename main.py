from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware  
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
def get_data():
    return {"msg": "Hello from FastAPI!"}

@app.get("/")
def read_root():
    return {"message": "Hello World"}

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return {"received_item": item}

