from typing import List

from card import Card
from player import Player
from dealer import Dealer
from deck import Deck


class Game:
    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
        self.bet_amount = 0
        self.winnings = 0

    def start_game(self):
        self.player.clear_hand()
        self.dealer.clear_hand()
        self.deck.shuffle()
        self.bet_amount = 0
        self.winnings = 0

    def place_bet(self, bet_amount: int):
        self.bet_amount = bet_amount

    def deal_initial_cards(self):
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

    def hit(self):
        self.player.add_card(self.deck.deal_card())

    def stand(self):
        while self.dealer.should_hit():
            self.dealer.add_card(self.deck.deal_card())

    def double_down(self):
        self.bet_amount *= 2
        self.player.add_card(self.deck.deal_card())
        self.stand()

    def calculate_score(self, hand: List[Card]) -> int:
        score = sum(card.get_value() for card in hand)
        aces = sum(card.get_rank() == 'A' for card in hand)

        while score > 21 and aces > 0:
            score -= 10
            aces -= 1

        return score

    def calculate_winnings(self, outcome: str):
        if outcome == 'win':
            self.winnings = self.bet_amount
        elif outcome == 'lose':
            self.winnings = -self.bet_amount
        else:
            self.winnings = 0

    def display_game_state(self):
        player_hand = self.player.get_hand()
        dealer_hand = self.dealer.get_hand()

        print("Player's hand:")
        for card in player_hand:
            print(card.get_rank(), "of", card.get_suit())

        print("\nDealer's hand:")
        for card in dealer_hand:
            print(card.get_rank(), "of", card.get_suit())

    def display_game_outcome(self, outcome: str):
        if outcome == 'win':
            print("You win!")
        elif outcome == 'lose':
            print("You lose!")
        else:
            print("It's a tie!")

    def display_winnings(self):
        print("Winnings:", self.winnings)

    def play_again(self):
        choice = input("Do you want to play again? (yes/no): ")
        return choice.lower() == 'yes'
