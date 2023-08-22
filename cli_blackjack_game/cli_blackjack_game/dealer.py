from typing import List

from card import Card


class Dealer:
    def __init__(self):
        self.hand = []
        self.score = 0

    def add_card(self, card: Card):
        self.hand.append(card)

    def clear_hand(self):
        self.hand = []

    def get_hand(self) -> List[Card]:
        return self.hand

    def get_score(self) -> int:
        return self.score

    def should_hit(self) -> bool:
        return self.score < 17
