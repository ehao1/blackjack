from typing import List

from fastapi import FastAPI
# from pydantic import BaseModel
# ^^^ used for database management
from fastapi.middleware.cors import CORSMiddleware
from deck import Deck

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
def read_root():
    return "Test"

@app.get("/drawCard")
def drawCard():
    deck = Deck(1)
    return deck.draw()


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}