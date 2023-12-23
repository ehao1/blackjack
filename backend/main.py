from typing import List

from fastapi import FastAPI
# from pydantic import BaseModel
# ^^^ used for database management
from fastapi.middleware.cors import CORSMiddleware
from card_constants import Card, CardSuit, CardValue, CountValue

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB: List[Card] = [
    Card(CardValue.ACE, CardSuit.DIAMOND),
    Card(CardValue.TWO, CardSuit.CLUB),
    Card(CardValue.THREE, CardSuit.SPADE),

]

@app.get("/api")
def read_root():
    return DB


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}