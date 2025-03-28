import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Display
FPS = 10
FPS_MAX = 26
FramePerSec = pygame.time.Clock()

Width, Height, Grid = 800, 800, 20

display = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Snake")

# Snake and Food
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"
food = (random.randint(0, Width // Grid - 1) * Grid,
        random.randint(0, Height // Grid - 1) * Grid)

def draw_food():
    pygame.draw.rect(display, (189, 17, 11), (food[0], food[1], Grid, Grid))
draw_food()

#Game Over and Score
score = 0
font = pygame.font.Font(None, 56)
font2 = pygame.font.Font(None, 36)
text = font.render("Game Over", 1, (224, 224, 11))
def game_over():
    display.blit(text, (300, 300))
    text_score = font2.render(f"Total Score: {score}", True, (224, 224, 11))
    display.blit(text_score, (330, 350))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

# Main Loop
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

    #Snake movement
    x, y = snake[0] 
    if direction == "UP":
        y -= Grid
    if direction == "DOWN":
        y += Grid
    if direction == "LEFT":
        x -= Grid
    if direction == "RIGHT":
        x += Grid

    #Borders
    if (x >= Width or x < 0 or y < 0 or y >= Height) or (x, y) in snake[1:]:
        game_over()
        
    #Checking if a snake has eaten food
    if (x, y) == food:
        food = (random.randint(0, Width // Grid - 1) * Grid,
                random.randint(0, Height // Grid - 1) * Grid)
        score += 1
        if score % 5 == 0:
            FPS = min(FPS + 2, FPS_MAX)
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
    
    #Draw score
    text_score = font2.render(f"Your Score: {score}", True, (224, 224, 11))
    display.blit(text_score, (10, 10))
    
    pygame.display.update()
    FramePerSec.tick(FPS)