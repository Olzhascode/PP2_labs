import pygame, sys, psycopg2
from pygame.locals import *
import random, time
from collections import deque

pygame.init()

# Connect to the database
conn = psycopg2.connect(
    dbname="snake_db",
    user="postgres",
    password="Kesha2412:)",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Display settings
FPS = 10
FPS_MAX = 40
FramePerSec = pygame.time.Clock()

def get_player_name():
    name = ''
    font_big = pygame.font.SysFont(None, 48)
    font_small = pygame.font.SysFont(None, 32)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name:
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode if event.unicode.isprintable() else ''

        display.fill((0, 0, 0))
        display.blit(font_big.render("Enter your nickname:", True, (255, 255, 255)), (200, 300))
        display.blit(font_small.render(name, True, (224, 224, 11)), (200, 360))
        pygame.display.flip()


Width, Height, Grid = 800, 800, 20
display = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Snake")
nickname = get_player_name()


# Snake and Food
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"
food = (random.randint(0, Width // Grid - 1) * Grid,
        random.randint(0, Height // Grid - 1) * Grid)
food_weight = random.randint(1, 3)

# Walls per level 
levels = [
    [],  
    [(x, 200) for x in range(300, 500, Grid)],
    [(400, y) for y in range(300, 500, Grid)],  
    [(x, 400) for x in range(100, 300, Grid)] + [(x, 400) for x in range(500, 700, Grid)]  
]
current_level = 0
walls = levels[current_level]

# Food timer
food_timer = 0
food_time_max = 60

# Check if the food is reachable 
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

# Generate new food at a reachable location
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

# Draw the food on the screen
def draw_food():
    pygame.draw.rect(display, (189, 17, 11), (food[0], food[1], Grid, Grid))

# Game Over and Score
score = 0
font = pygame.font.Font(None, 56)
font2 = pygame.font.Font(None, 36)
text = font.render("Game Over", 1, (224, 224, 11))


def game_over():
    global score, nickname
    display.blit(text, (300, 300))
    text_score = font2.render(f"Total Score: {score}", True, (224, 224, 11))
    display.blit(text_score, (330, 350))
    pygame.display.flip()
    time.sleep(2)
    insert(nickname, score, current_level)  # Save score and nickname to DB
    pygame.quit()
    sys.exit()


def insert(nickname, score, current_level):
    # Check if player already exists
    cur.execute("SELECT score FROM snake_player_db WHERE nickname = %s", (nickname,))
    result = cur.fetchone()

    if result:
        old_score = result[0]
        print(f"Existing score for {nickname}: {old_score}, New score: {score}")
        if score > old_score:
            cur.execute("""
                UPDATE snake_player_db
                SET score = %s, level = %s
                WHERE nickname = %s
            """, (score, current_level, nickname))
            print("Score updated.")
        else:
            print("New score is not higher. No update.")
    else:
        cur.execute("""
            INSERT INTO snake_player_db (nickname, score, level)
            VALUES (%s, %s, %s)
        """, (nickname, score, current_level))
        print("New player inserted.")

    conn.commit()


# Main game loop
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

    # Check for collisions with walls or snake's body
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

    # Add new head to the snake
    snake.insert(0, (x, y))

    # Draw everything on the screen
    display.fill("BLACK")
    draw_food()

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(display, (13, 117, 16), (segment[0], segment[1], Grid, Grid))

    # Draw walls
    for wall in walls:
        pygame.draw.rect(display, (100, 100, 100), (wall[0], wall[1], Grid, Grid))

    # Draw score and level
    text_score = font2.render(f"Score: {score}  Level: {current_level + 1}", True, (224, 224, 11))
    display.blit(text_score, (10, 10))

    pygame.display.update()
    FramePerSec.tick(FPS)
