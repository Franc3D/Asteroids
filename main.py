import pygame
from constants import *

"""
A game needs to go through 3 steps:
1) Check for player inputs
2) Update the game world
3) Draw the game to the screen
"""

def main():
    pygame.init()  # Initialize all imported pygame modules

    # Set a new GUI using pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Draw the game to the screen
    while True:
        screen.fill()

    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
