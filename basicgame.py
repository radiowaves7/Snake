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

#Import dependancies
import pygame
import time
import random

# Global Settings
score = 0
snake_speed = 15

# Window size
window_x = 720
window_y = 480
window_xmid = window_x/2
window_ymid = window_y/2

# Colours (R,G,B)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

# Initialise the game
pygame.init()

# Set up game window
pygame.display.set_caption("Snake")
game_window = pygame.display.set_mode((window_x, window_y))
# FPS controller
FPS = pygame.time.Clock()

# Initialise the snake position
snake_pos = [100, 50]
# Initialise the snake body
snake_body = [
    [snake_pos[0], snake_pos[1]],
    [snake_pos[0]-10, snake_pos[1]],
    [snake_pos[0]-20, snake_pos[1]],
    [snake_pos[0]-30, snake_pos[1]]
    ]

# Initialise fruit position
fruit_pos = [random.randrange(1, (window_x//10)) * 10,
    random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

# Set the deafult snake direction, moving right
# 0 = Up
# 1 = Right
# 2 = Down
# 3 = Left
snake_direction = 1
change_direction = snake_direction

def show_score(choice, color, font, size):
    """
    A fucntion which creates a surface and rectangle for score
    and displays the score.
    """
    # Set the score font
    score_font = pygame.font.SysFont(font, size)
    # Create the display surface
    score_surface = score_font.render('Score : ' + str(score), True, color)
    # Create a rectangle for the text surface
    score_rect = score_surface.get_rect()
    # Display the text
    game_window.blit(score_surface, score_rect)

def game_over():
    """
    """
    # Creates a font
    my_font = pygame.font.SysFont('times new roman', 50)
    # Create a text surface
    game_over_surface = my_font.render(
        'Your score is : ' + str(score), True, red)
    # Create a rectangle for the text surface
    game_over_rect = game_over_surface.get_rect()
    # Setting position of the text
    game_over_rect.midtop = (window_xmid, window_ymid/2)
    # Draw tex to the display
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # Delay program by 2 seconds then quit and exit
    time.sleep(2)
    pygame.quit()
    exit()

# Game loop
while True:
    # Key event handler
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_direction = 0
            if event.key == pygame.K_RIGHT:
                change_direction = 1
            if event.key == pygame.K_DOWN:
                change_direction = 2
            if event.key == pygame.K_LEFT:
                change_direction = 3
    
    # Stop the snake going back on itself
    if change_direction == 0 and snake_direction == 2:
        change_direction = 2
    if change_direction == 1 and snake_direction == 3:
        change_direction = 3
    if change_direction == 2 and snake_direction == 0:
        change_direction = 0
    if change_direction == 3 and snake_direction == 1:
        change_direction = 1
    
    # Change the snakes direction
    snake_direction = change_direction
    
    # Moving the snake
    if snake_direction == 0:
        snake_pos[1] -=10
    if snake_direction == 1:
        snake_pos[0] +=10
    if snake_direction == 2:
        snake_pos[1] +=10
    if snake_direction == 3:
        snake_pos[0] -=10

    # Snake body growing
    # if snake head and fruit collide increment score
    snake_body.insert(0, list(snake_pos))
    if snake_pos == fruit_pos:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop()
    
    # Respawn fruit
    if not fruit_spawn:
        fruit_pos = [
            random.randrange(1, window_x//10) * 10,
            random.randrange(1, window_y//10) * 10
            ]
        fruit_spawn = True
    
    # Update the game drawings
    # Fill the background
    game_window.fill(black)
    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
            pygame.Rect(pos[0], pos[1], 10, 10)
            )
    # Draw the fruit
    pygame.draw.rect(game_window, white,
        pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10)
        )
    
    # Game over conditions
    # Outside of game window
    if snake_pos[0] < 0:
        game_over()
    if (snake_pos[0] > (window_x - 10)):
        game_over()
    if snake_pos[1] < 0:
        game_over()
    if (snake_pos[1] > (window_y - 10)):
        game_over()
    # Touching snake body
    for block in snake_body[1:]:
        if (snake_pos[0] == block[0] and snake_pos[1] == block[1]):
            game_over()
    
    
    # Display the current score
    show_score(1, white, 'times new roman', 20)

    # Refresh the sceen
    pygame.display.update()

    # Frames Per Second / Refresh Rate
    FPS.tick(snake_speed)
