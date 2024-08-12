from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  #Connection of Frontend

app = FastAPI()

#Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return "Hello, World! Serega 111"

@app.get("/serega")
def serega():
    return "Serega!!!!1111122222222"