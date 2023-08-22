import curses
from typing import List, Tuple

class Snake:
    def __init__(self, x: int, y: int):
        self.body = [(x, y)]
        self.head = (x, y)
        self.direction = (0, 1)

    def move(self) -> None:
        x, y = self.head
        dx, dy = self.direction
        new_head = (x + dx, y + dy)
        self.body.insert(0, new_head)
        self.head = new_head
        self.body.pop()

    def change_direction(self, key: int) -> None:
        if key == curses.KEY_UP:
            self.direction = (-1, 0)
        elif key == curses.KEY_DOWN:
            self.direction = (1, 0)
        elif key == curses.KEY_LEFT:
            self.direction = (0, -1)
        elif key == curses.KEY_RIGHT:
            self.direction = (0, 1)

    def eat_food(self, food: 'Food') -> None:
        self.body.append(food.position)

    def check_collision(self, width: int, height: int) -> bool:
        x, y = self.head
        if x < 0 or x >= width or y < 0 or y >= height:
            return True
        if self.head in self.body[1:]:
            return True
        return False


class Food:
    def __init__(self, width: int, height: int):
        self.position = (0, 0)
        self.width = width
        self.height = height

    def generate(self) -> None:
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        self.position = (x, y)


class Game:
    def __init__(self, width: int, height: int, speed: int):
        self.score = 0
        self.width = width
        self.height = height
        self.speed = speed
        self.game_over = False
        self.paused = False
        self.snake = Snake(width // 2, height // 2)
        self.food = Food(width, height)
        self.food.generate()

    def start(self) -> None:
        curses.wrapper(self.main)

    def main(self, stdscr) -> None:
        curses.curs_set(0)
        stdscr.nodelay(1)
        stdscr.timeout(self.speed)

        while True:
            if not self.paused:
                self.update()
            self.draw(stdscr)

            key = stdscr.getch()
            self.handle_input(key)

            if self.game_over:
                self.game_over_screen(stdscr)
                key = stdscr.getch()
                if key == ord('r'):
                    self.restart()
                else:
                    break

    def update(self) -> None:
        self.snake.move()

        if self.snake.head == self.food.position:
            self.snake.eat_food(self.food)
            self.score += 1
            self.food.generate()

        if self.snake.check_collision(self.width, self.height):
            self.game_over = True

    def draw(self, stdscr) -> None:
        stdscr.clear()
        stdscr.border()

        for x, y in self.snake.body:
            stdscr.addch(y, x, '*')

        x, y = self.food.position
        stdscr.addch(y, x, '+')

        stdscr.addstr(0, 2, f"Score: {self.score}")

        if self.paused:
            stdscr.addstr(self.height // 2, self.width // 2 - 4, "Paused")

        stdscr.refresh()

    def handle_input(self, key: int) -> None:
        if key == ord('q'):
            self.game_over = True
        elif key == ord('p'):
            self.paused = not self.paused
        else:
            self.snake.change_direction(key)

    def game_over_screen(self, stdscr) -> None:
        stdscr.clear()
        stdscr.border()
        stdscr.addstr(self.height // 2, self.width // 2 - 9, "Game Over")
        stdscr.addstr(self.height // 2 + 1, self.width // 2 - 15, "Press 'r' to restart or 'q' to quit")
        stdscr.refresh()

    def restart(self) -> None:
        self.score = 0
        self.game_over = False
        self.paused = False
        self.snake = Snake(self.width // 2, self.height // 2)
        self.food.generate()
