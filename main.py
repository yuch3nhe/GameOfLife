import pygame
import time
import random
import numpy as np
import os
import grid
import coloured_grid
#import gameEngine

# size of the screen
width, height = 1000, 580
size = (width, height)

# game display and speed of the cells
pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 10

# colour of the grid and cells
black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)

#size of the grid
scaler = 20
offset = 1
Grid = grid.Grid(width, height, scaler, offset)
Grid.random2d_array()  # produces random cells
Grid2 = coloured_grid.Grid(width, height, scaler, offset)
Grid2.random2d_array()  # produces random cells


# to quit, pause and resume the game
paused = False
run = True
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
    if paused == True:
        continue


    Grid.Conway(off_color = white, on_color=blue1, surface=screen)
    pygame.display.update()

pygame.quit()

# organism = #initial state
# gameEngine g = new gameEngine(organism)
