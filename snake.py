# Basic Snake game, code by Maher Suleiman

# Imports
import pygame as pg
from random import randrange

# Sets up window and clock for game
window = 1000
screen = pg.display.set_mode([window] * 2)
clock = pg.time.Clock()

# Variables
tileSize, length, time, timeStep = 50, 1, 0, 110
range = (tileSize // 2, window - tileSize // 2, tileSize)
getRandPos = lambda: [randrange(*range), randrange(*range)]

# Set up snake
snake = pg.rect.Rect([0, 0, tileSize - 2, tileSize - 2])
snake.center = getRandPos()
segments = [snake.copy()]
snakeDir = (0, 0)

# Food
food = snake.copy()
food.center = getRandPos()

# Main game loop
while True:
    for event in pg.event.get():
        # Exits out the game if esc is pressed
        if event.type == pg.QUIT:
            exit()
        # Moves snake by checking if WASD were pressed, if so, moves snake based on the coordinate
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                snakeDir = (0, -tileSize)
            if event.key == pg.K_s:
                snakeDir = (0, tileSize)
            if event.key == pg.K_a:
                snakeDir = (-tileSize, 0)
            if event.key == pg.K_d:
                snakeDir = (tileSize, 0)
        
        # Makes background black
        screen.fill('black')

        # Checks if snake has hit a border and if it has it resets its position and length
        if snake.left < 0 or snake.right > window or snake.top < 0 or snake.bottom > window:
            snake.center, food.center = getRandPos(), getRandPos()
            length, snakeDir = 1, (0,0)
            segments = [snake.copy()]
        # Increases snake length by 1 if it eats the food
        if snake.center == food.center:
            length += 1
            food.center = getRandPos()
        #Drawing objects to screen
        pg.draw.rect(screen, 'white', food)
        [pg.draw.rect(screen, 'blue', segment) for segment in segments]
        # Moves snake
        timeNow = pg.time.get_ticks()
        if timeNow - time > timeStep:
            time = timeNow
            snake.move_ip(snakeDir)
            segments.append(snake.copy())
            segments = segments[-length:]

        pg.display.flip()
        # Sets framerate to 60fps
        clock.tick(60)
            
        
            
