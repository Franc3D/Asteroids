# Import a LIBRARY
import pygame
# 
from constants import *

"""
A game needs to go through 3 steps:
1) Check for player inputs
2) Update the game world
3) Draw the game to the screen
"""

def main():
    pygame.init()  # Initialize all imported pygame modules
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Set a new GUI using pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # 3) Draw the game to the screen
    while True:
        # Make exit button work
        # This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



        screen.fill(0)  # Fill the screen with black
        
        # Use this at the very end of the loop to refresh the display
        pygame.display.flip()

    


if __name__ == "__main__":
    main()
