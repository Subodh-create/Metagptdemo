import curses
from game import Game

def main(stdscr):
    # Set up the game window
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Get the window dimensions
    height, width = stdscr.getmaxyx()

    # Create a new game instance
    game = Game(width, height)

    # Start the game loop
    while True:
        # Update the game state
        game.update()

        # Draw the game screen
        game.draw(stdscr)

        # Handle user input
        key = stdscr.getch()
        game.handle_input(key)

        # Check if the game is over
        if game.game_over:
            game.game_over_screen(stdscr)
            key = stdscr.getch()
            if key == ord('r'):
                game.restart()
            else:
                break

# Start the game
if __name__ == "__main__":
    curses.wrapper(main)
