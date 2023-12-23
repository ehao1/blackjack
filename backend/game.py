from deck import Card, Deck
from typing import List

# class Game:
class Game:
    def __init__(self, num_users: int, num_decks: int) -> None:
        """Toggles a bunch of options!"""
        self.num_users = num_users
        self.users: List[User]
        for _ in range(num_users):
            #create a new User
            user = User(100)
            self.users.append(user)

        self.deck = Deck(num_decks)

        self.dealer = Dealer()
        return

    # Game.start() will start a game
    def new_round(self) -> None:
        # clear everyone's hands
        for user in self.users:
            user._clear_hand()
        self.dealer._clear_hand()

        # deal two cards to dealer
        self.dealer.hit()
        self.dealer.hit()

        # deal two cards to every user
        for user in self.users:
            user.hit()

    def prompt_input(self, player) -> None:
        """Determine user acton from here"""


    # Dealer
    # Players (1 for now)
    # Deck

    # Round.start()
    # has a deck
    # has a dealer
    # has a player
    
    # start game
    

class Hand:
    """Holds a list of cards a Player has"""
    def __init__(self) -> None:
        self.cards = List[Card] = []
        self.card_score = 0
    
    
    def add_card(self, card: Card) -> int:
        """Adds a card to Hand.
            Returns value of Hand.
        """
        self.card_score += card.value
        return self.card_score

    def clear(self) -> None:
        self.cards = []

class Player:
    def __init__(self) -> None:
        self.deck: Deck = deck
        self.hand: Hand = Hand()

    def hit(self) -> int:
        """Player hits the deck."""   
        card: Card = self.deck.draw() 
        return self.hand.add_card(card)

    def stand(self) -> int:
        """Player stands."""
        return self.hand.card_score

    def _clear_hand(self) -> None:
        self.hand.clear()
    
class Dealer(Player):
    pass

class User(Player):
    def __init__(self, starting_cash: int) -> None:
        Player.__init__(self) 
        self.cash: int = starting_cash
        self.split_hand: Hand = Hand()

    def _clear_hand(self) -> None:
        super()._clear_hand()
        self.split_hand.clear()

    def bet(self, cash: int) -> None:
        """Player bets"""
    
    def insurance(self) -> None:
        """Player does insurance"""

    def split(self) -> None:
        """Player splits uh oh"""
        return


    self.shuffle()