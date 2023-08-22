from typing import List
import random


class Card:
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def get_suit(self) -> str:
        return self.suit

    def get_rank(self) -> str:
        return self.rank

    def get_value(self) -> int:
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)


class Deck:
    def __init__(self):
        self.cards = []
        self.initialize_deck()

    def initialize_deck(self):
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self) -> Card:
        if len(self.cards) == 0:
            raise Exception("No cards left in the deck.")
        return self.cards.pop()
