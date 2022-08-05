from statistics import variance
from classes.deck import Deck

bicycle = Deck()

bicycle.show_cards()


class Card:

    def __init__(self, value, suit):
        self.cost = value
        self.value = ['A', '2', '3', '4', '5', '6',
                      '7', '8', '9', '10', 'J', 'Q', 'K']
        self.suit = ["spades", "hearts", "clubs", "diamonds"]

    def card_info(self):
        if self.cost >= 10:
            return 10
        elif self.cost == 1:
            return 11
        return self.cost

    def show(self):
        print(self.value)
        print(self.suit)
