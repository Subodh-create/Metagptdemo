## utils.py

import os
from colorama import Fore, Style

class Utils:
    @staticmethod
    def clear_screen():
        """
        Clears the console screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_colorful_message(message: str, color: str):
        """
        Prints a colorful message to the console.

        Args:
            message (str): The message to be printed.
            color (str): The color of the message.
        """
        print(f"{color}{message}{Style.RESET_ALL}")
