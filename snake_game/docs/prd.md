## Original Requirements:

The boss wants a command-line snake game implemented in Java.

## Product Goals:
```python
[
    "Create a command-line snake game in Java",
    "Ensure the game is playable and enjoyable",
    "Implement basic game mechanics and scoring system"
]
```

## User Stories:
```python
[
    "As a player, I want to be able to control the snake's movement using arrow keys",
    "As a player, I want the snake to grow longer when it eats food",
    "As a player, I want the game to end if the snake hits the wall or itself",
    "As a player, I want to see my current score displayed on the screen",
    "As a player, I want to be able to restart the game after it ends"
]
```

## Competitive Analysis:
```python
[
    "Python Snake Game: A popular snake game implemented in Python with a simple user interface",
    "Java Snake Game: Another snake game implemented in Java with customizable settings",
    "C++ Snake Game: A snake game implemented in C++ with advanced graphics and sound effects",
    "Mobile Snake Game: A mobile version of the snake game with touch controls and multiplayer mode",
    "Web Snake Game: A snake game playable in a web browser with online leaderboard",
    "Snake Game App: A mobile app with various snake game modes and power-ups",
    "Classic Snake Game: A simple snake game with retro graphics and classic gameplay"
]
```

## Competitive Quadrant Chart:
```mermaid
quadrantChart
    title Reach and engagement of snake game competitors
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 Java Snake Game: [0.4, 0.5]
    quadrant-2 Python Snake Game: [0.6, 0.4]
    quadrant-3 Web Snake Game: [0.7, 0.8]
    quadrant-4 Mobile Snake Game: [0.8, 0.7]
    "C++ Snake Game": [0.3, 0.3]
    "Snake Game App": [0.5, 0.6]
    "Classic Snake Game": [0.2, 0.2]
    "Our Target Product": [0.5, 0.6]
```

## Requirement Analysis:
The product should be a command-line snake game implemented in Java. It should have basic game mechanics such as snake movement, food generation, and collision detection. The game should end if the snake hits the wall or itself. The player's score should be displayed on the screen. The game should allow the player to restart after it ends.

## Requirement Pool:
```python
[
    ("Implement snake movement using arrow keys", "P0"),
    ("Implement snake growth when it eats food", "P0"),
    ("Implement collision detection with wall and snake body", "P0"),
    ("Display the player's score on the screen", "P1"),
    ("Allow the player to restart the game after it ends", "P1")
]
```

## UI Design draft:
The game will be displayed in the command-line interface. The snake will be represented by a character, such as an asterisk (*), and the food will be represented by a different character, such as a plus sign (+). The player will control the snake's movement using arrow keys. The score will be displayed at the top of the screen. The game over message will be displayed when the game ends, along with an option to restart the game.

## Anything UNCLEAR:
There are no unclear points.