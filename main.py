# Import a LIBRARY
import pygame
import sys
# 
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


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
    
    # set a new clock object to control the frame rate
    clock = pygame.time.Clock()
    


    # Creating new groups to better organize the update() and draw() methods
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    # BLACK MAGIC ALERT
    # the code bellow ADDS a method to the player class DESPITE BEING IN MAIN !!! This will affect all player objects identically
    Player.containers = (updatable, drawable)   # Add before any player object declaration
    # .containers only works due to pygame looking for that exact name. 

    # Create the player controlled character and place it in the center of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   
    dt = 0 # delta time, the time since the last frame



    



    

    # 3) Draw the game to the screen
    while True:
        # Make exit button work
        # This will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        
        updatable.update(dt)

        display_gameover = False
        for asteroid in asteroids:
            if player.collide(asteroid):    # if player collide with asteroid
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if shot.collide(asteroid):  # if shot connects with asteroid
                    shot.kill()             # from pygame.sprite.Sprite.kill() it removes the object from all its groups
                    asteroid.split()



        screen.fill(0)  # Fill the screen with black

        # make the player appear on the screen
        for player_to_draw in drawable:
            player_to_draw.draw(screen)



        # Use this at the very end of the loop to refresh the display
        pygame.display.flip()

        # make the game wait for a total of 1/60th of a second since the start of the loop
        dt = clock.tick(60) / 1000      # divide by 1000 to write seconds instead of milliseconds


    


if __name__ == "__main__":
    main()
