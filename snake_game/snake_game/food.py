import random
from typing import Tuple

class Food:
    def __init__(self, width: int, height: int):
        self.position = (0, 0)
        self.width = width
        self.height = height

    def generate(self) -> None:
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        self.position = (x, y)
