# File holding constants
from enum import Enum

class CardSuit(Enum):
    SPADE = 1
    HEART = 2
    CLUB = 3
    DIAMOND = 4

class CountValue(Enum):
    NEG = -1
    ZERO = 0
    POS = 1

class CardValue(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13