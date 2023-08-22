import click
from tabulate import tabulate
from colorama import Fore, Style
from game_logic import Game
from ascii_art import AsciiArt
from utils import Utils


class CLI:
    def __init__(self):
        self.game = Game()
        self.ascii_art = AsciiArt()

    def start(self):
        self.game.start_game()
        self.print_welcome_message()
        self.play()

    def print_welcome_message(self):
        Utils.clear_screen()
        Utils.print_colorful_message("Welcome to CLI Blackjack Game!", Fore.GREEN)
        print("Instructions:")
        print("- Place your bet.")
        print("- Choose an action: hit, stand, or double down.")
        print("- Try to get as close to 21 without going over.")
        print("- The dealer will also try to get as close to 21.")
        print("- The player with the highest score wins.")
        print()

    def get_bet_amount(self) -> int:
        while True:
            try:
                bet_amount = int(input("Enter your bet amount: "))
                if bet_amount <= 0:
                    raise ValueError
                return bet_amount
            except ValueError:
                print("Invalid bet amount. Please enter a positive integer.")

    def print_game_state(self):
        Utils.clear_screen()
        player_hand = self.game.player.get_hand()
        dealer_hand = self.game.dealer.get_hand()

        print("Player's hand:")
        for card in player_hand:
            card_art = self.ascii_art.get_card_art(card)
            print(card_art)

        print("\nDealer's hand:")
        dealer_card = dealer_hand[0]
        dealer_card_art = self.ascii_art.get_card_art(dealer_card)
        print(dealer_card_art)
        print("Hidden card")

    def get_action(self) -> str:
        while True:
            action = input("Choose an action (hit, stand, double down): ")
            if action.lower() in ['hit', 'stand', 'double down']:
                return action.lower()
            else:
                print("Invalid action. Please choose from hit, stand, or double down.")

    def print_game_outcome(self, outcome: str):
        if outcome == 'win':
            Utils.print_colorful_message("You win!", Fore.GREEN)
        elif outcome == 'lose':
            Utils.print_colorful_message("You lose!", Fore.RED)
        else:
            Utils.print_colorful_message("It's a tie!", Fore.YELLOW)

    def print_winnings(self):
        winnings = self.game.winnings
        if winnings > 0:
            Utils.print_colorful_message(f"Winnings: {winnings}", Fore.GREEN)
        elif winnings < 0:
            Utils.print_colorful_message(f"Winnings: {winnings}", Fore.RED)
        else:
            Utils.print_colorful_message("Winnings: 0", Fore.YELLOW)

    def play_again(self) -> bool:
        while True:
            choice = input("Do you want to play again? (yes/no): ")
            if choice.lower() == 'yes':
                return True
            elif choice.lower() == 'no':
                return False
            else:
                print("Invalid choice. Please enter yes or no.")

    def play(self):
        while True:
            bet_amount = self.get_bet_amount()
            self.game.place_bet(bet_amount)
            self.game.deal_initial_cards()

            while True:
                self.print_game_state()
                action = self.get_action()

                if action == 'hit':
                    self.game.hit()
                elif action == 'stand':
                    self.game.stand()
                elif action == 'double down':
                    self.game.double_down()

                player_score = self.game.calculate_score(self.game.player.get_hand())
                dealer_score = self.game.calculate_score(self.game.dealer.get_hand())

                if player_score > 21:
                    outcome = 'lose'
                    break
                elif dealer_score > 21:
                    outcome = 'win'
                    break
                elif action == 'stand':
                    if player_score > dealer_score:
                        outcome = 'win'
                    elif player_score < dealer_score:
                        outcome = 'lose'
                    else:
                        outcome = 'tie'
                    break

            self.game.calculate_winnings(outcome)
            self.print_game_state()
            self.print_game_outcome(outcome)
            self.print_winnings()

            if not self.play_again():
                break


@click.command()
def main():
    cli = CLI()
    cli.start()


if __name__ == '__main__':
    main()
