from typing import List, TypedDict
import random
from card_constants import CardSuit, CardValue, CountValue

class Card(tuple):

    def __new__(cls, value, suit):
        assert isinstance(value, CardValue)
        assert isinstance(suit, CardSuit)
        return tuple.__new__(cls, (value, suit))
    
    @property
    def value(self):
        return self[0]

    @property
    def suit(self):
        return self[1]
class DeckCountTable(TypedDict):
    card: Card
    total_count: int

"""Creates a deck object.
"""
class Deck:

    def __init__(self, num_decks: int) -> None:
        """Draws a card from the deck.
        """
        self.num_decks = num_decks
        self.shuffle()

    def shuffle(self) -> None:
        """Shuffles the deck randomly
        """
        self.count_table: DeckCountTable = {}
        self.ordered_list: List[Card] = []
        self.deck_position = 0
        # self.running_count = 0
        # self.true_count = 0

        for suit in CardSuit:
            for value in CardValue:
                card = Card(value, suit)
                self.count_table[card] = self.num_decks
                for _ in range(self.num_decks):
                    self.ordered_list.append(card)
                

        # randomize the array order
        random.shuffle(self.ordered_list)
        return
            
    def draw(self) -> Card:
        """Draws a card from the deck.
        """
        return_card: Card = self.ordered_list[self.deck_position]

        self.count_table[return_card] -= 1
        self.deck_position += 1

        # handle logic for true and running count

        return return_card

    # returns all cards in deck

    # returns true running count

