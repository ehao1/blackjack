from deck import Card, Deck
import random


def test_one_deck_draw():

   random.seed(10)
   deck = Deck(1)

   copy_deck_list = deck.ordered_list.copy()

   assert len(copy_deck_list) == 52

   for i in range(len(copy_deck_list)):
      card: Card = deck.draw()
      assert(card == copy_deck_list[i])
      assert(deck.count_table[card] == 0)
   
def test_two_deck():

   random.seed(10)
   deck = Deck(2)

   copy_deck_list = deck.ordered_list.copy()

   assert len(copy_deck_list) == 104

   for i in range(len(copy_deck_list)):
      card: Card = deck.draw()
      assert(card == copy_deck_list[i])
