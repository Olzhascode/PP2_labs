import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

#FPS
FPS = 10
FramePerSec = pygame.time.Clock()

#Screen
Width = 800
Height = 800
Grid = 20
display = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Snake")

#Snake
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"

#Food
food = (random.randint(0, Width // Grid - 1) * Grid,
        random.randint(0, Height // Grid - 1) * Grid)

def draw_food():
    pygame.draw.rect(display, (189, 17, 11), (food[0], food[1], Grid, Grid))

draw_food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

    #Snake control
    x, y = snake[0] #snake head
    if direction == "UP":
        y -= Grid
    if direction == "DOWN":
        y += Grid
    if direction == "LEFT":
        x -= Grid
    if direction == "RIGHT":
        x += Grid

    #Checking if a snake has eaten food
    if snake[0] == food:
        food = (random.randint(0, Width // Grid - 1) * Grid,
                random.randint(0, Height // Grid - 1) * Grid)
    else:
        snake.pop()

    #Adding new part of snake
    snake.insert(0, (x, y))

    #Screen cleaning
    display.fill("BLACK")
    
    #Draw food
    draw_food()
    
    #Draw snake
    for segment in snake:
        pygame.draw.rect(display, (13, 117, 16), (segment[0], segment[1], Grid, Grid))

    pygame.display.update()
    FramePerSec.tick(FPS)