from typing import List

suits: List[str] = ['hearts', 'spades', 'diamonds', 'clubs']
values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        return self


deck = [Card(value, suit) for value in values
                          for suit in suits]
