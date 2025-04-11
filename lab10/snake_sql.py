import pygame, sys
from pygame.locals import *
import random, time
from collections import deque

pygame.init()

# Display
FPS = 10
FPS_MAX = 40
FramePerSec = pygame.time.Clock()

Width, Height, Grid = 800, 800, 20
display = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Snake")

# Snake and Food
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"
food = (random.randint(0, Width // Grid - 1) * Grid,
        random.randint(0, Height // Grid - 1) * Grid)
food_weight = random.randint(1, 3)

# Walls per level 
levels = [
    [],  # Level 1 — no walls
    [(x, 200) for x in range(300, 500, Grid)],
    [(400, y) for y in range(300, 500, Grid)],  
    [(x, 400) for x in range(100, 300, Grid)] + [(x, 400) for x in range(500, 700, Grid)]  
]
current_level = 0
walls = levels[current_level]

# Food timer
food_timer = 0
food_time_max = 60

def is_food_reachable(start, target):
    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)
    blocked = set(snake[1:] + walls)

    while queue:
        x, y = queue.popleft()
        if (x, y) == target:
            return True
        for dx, dy in [(-Grid, 0), (Grid, 0), (0, -Grid), (0, Grid)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < Width and 0 <= ny < Height and
                (nx, ny) not in visited and (nx, ny) not in blocked):
                queue.append((nx, ny))
                visited.add((nx, ny))
    return False

def generate_food():
    global food, food_weight, food_timer
    attempts = 0
    while attempts < 100:
        f = (random.randint(0, Width // Grid - 1) * Grid,
             random.randint(0, Height // Grid - 1) * Grid)
        if f not in snake and f not in walls and is_food_reachable(snake[0], f):
            food = f
            break
        attempts += 1
    food_weight = random.randint(1, 3)
    food_timer = 0

def draw_food():
    pygame.draw.rect(display, (189, 17, 11), (food[0], food[1], Grid, Grid))

# Game Over and Score
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

    # Snake movement
    x, y = snake[0]
    if direction == "UP": y -= Grid
    if direction == "DOWN": y += Grid
    if direction == "LEFT": x -= Grid
    if direction == "RIGHT": x += Grid

    # Check for collisions
    if (x >= Width or x < 0 or y < 0 or y >= Height) or (x, y) in snake[1:] or (x, y) in walls:
        game_over()

    # Check if food is eaten
    if (x, y) == food:
        score += food_weight
        generate_food()
        food_timer = 0
        if score % 5 == 0:
            FPS = min(FPS + 2, FPS_MAX)
        if score // 10 > current_level and current_level < len(levels) - 1:
            current_level += 1
            walls = levels[current_level]
    else:
        snake.pop()

    # Food timer
    food_timer += 1
    if food_timer >= food_time_max:
        generate_food()

    # Add new head
    snake.insert(0, (x, y))

    # Draw everything
    display.fill("BLACK")
    draw_food()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(display, (13, 117, 16), (segment[0], segment[1], Grid, Grid))

    # Draw walls
    for wall in walls:
        pygame.draw.rect(display, (100, 100, 100), (wall[0], wall[1], Grid, Grid))

    # Draw score
    text_score = font2.render(f"Score: {score}  Level: {current_level + 1}", True, (224, 224, 11))
    display.blit(text_score, (10, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)
