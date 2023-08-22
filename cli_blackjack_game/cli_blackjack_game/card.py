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
