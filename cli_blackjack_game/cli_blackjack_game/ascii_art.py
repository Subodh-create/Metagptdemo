from card import Card


class AsciiArt:
    def __init__(self):
        pass

    def get_card_art(self, card: Card) -> str:
        """
        Returns the ASCII art representation of a card.

        Args:
            card (Card): The card object.

        Returns:
            str: The ASCII art representation of the card.
        """
        # ASCII art code for each card
        card_art = {
            "2": """
                 _______
                |2      |
                |       |
                |   ♠   |
                |       |
                |_______|
                """,
            "3": """
                 _______
                |3      |
                |       |
                |   ♠   |
                |       |
                |_______|
                """,
            "4": """
                 _______
                |4      |
                |       |
                |   ♠   |
                |       |
                |_______|
                """,
            "5": """
                 _______
                |5      |
                |       |
                |   ♠   |
                |       |
                |_______|
                """,
            "6": """
                 _______
                |6      |
                |       |
                |   ♠   |
                |       |
                |_______|
                """,
            "7": """
                 _______
                |7      |
                |       |
                |   ♠   |
                |       |
                |_______|
                """,
            "8": """
                 _______
                |8      |
                |       |
                |   ♠   |
                |       |
                |_______|
                """,
            "9": """
                 _______
                |9      |
                |       |
                |   ♠   |
                |       |
                |_______|
                """,
            "10": """
                 _______
                |10     |
                |       |
                |   ♠   |
                |       |
                |_______|
                """,
            "J": """
                 _______
                |J      |
                |       |
                |   ♠   |
                |       |
                |_______|
                """,
            "Q": """
                 _______
                |Q      |
                |       |
                |   ♠   |
                |       |
                |_______|
                """,
            "K": """
                 _______
                |K      |
                |       |
                |   ♠   |
                |       |
                |_______|
                """,
            "A": """
                 _______
                |A      |
                |       |
                |   ♠   |
                |       |
                |_______|
                """
        }

        rank = card.get_rank()
        return card_art[rank]
