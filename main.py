"""
Snake (Python) by Jack Gooding.

Snake was originally developed by a British company,
Gremlin Interactive, in 1976.

It is an interesting and skill based game,
which has been popular for generations.

The player's goal is to achieve as many points as possible
by collecting food for the snake.

The snake can be controlled by moving in it one of four directions.
If the snake's head collides with itself or a wall it dies, and the game
is ended, displaying the palyer's score.
"""
# Import dependancies
import pygame

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for colors (R,G,B)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

# Classes
# Snake Class
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super(Snake, self).__init__()
        self.direction = "UP"
        self.position = [100,50]
        self.body = [
            self.position,
            [self.position[0]-10, self.position[1]],
            [self.position[0]-20, self.position[1]],
            [self.position[0]-30, self.position[1]]
        ]
        self.surface = pygame.Surface((10,10))
        self.surface.fill(green)
        self.rectangle = self.surface.get_rect()
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rectangle.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rectangle.move_ip(0, 10)
        if pressed_keys[K_LEFT]:
            self.rectangle.move_ip(-10, 0)
        if pressed_keys[K_RIGHT]:
            self.rectangle.move_ip(10, 0)



# Functions
def main(self):
    """
    The main game function.
    """
    # Initialize pygame
    pygame.init()
    
    # Define constants for screen size
    window_x = 720
    window_y = 480
    
    # Create the screen object
    window = pygame.display.set_mode((window_x, window_y))

    # Fill the screen black
    window.fill(black)

    # Create a surface of tuple (length,width)
    surface = pygame.Surface((50,50))
    # Fill the surface white
    surface.fill(white)
    rectangle = surface.get_rect()
    # Define surface center
    surface_center = (
        (window_x-surface.get_width())/2,
        (window_y-surface.get_height())/2
    )
    # Draw the surface onto the center of the screen
    window.blit(surface, surface_center)
    pygame.display.flip()

    # Main game loop
    running = True
    while running:
        # Check events
        for event in pygame.event.get():
            # Was a key pressed?
            if event.type == KEYDOWN:
                # Was it the escape key?
                if event.key == K_ESCAPE:
                    # Exit the loop
                    running = False
            # Was the window close button clicked?
            elif event.type == QUIT:
                # Exit the loop
                running = False
        
        # Get all the keys currently presssed
        pressed_keys = pygame.keys.get_pressed()

        # Update the player sprite, based on keys pressed
        

# Check for import
if "__name__" == "__main__":
    # Initialise
    main()