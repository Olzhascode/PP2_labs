import pygame

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Canvas
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

colors = {"red": RED, "blue": BLUE, "green": GREEN, "erase": WHITE}
color = "red"

# Modes
radius = 10
mouse_down = False
running = True
starting_position = None
last_position = None

mode_draw = "Draw"
mode_rect = "Rect"
mode_circle = "Circle"
mode = mode_draw # defualt mode

# Main Loop
while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Colors
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = "red" 
            elif event.key == pygame.K_g:
                color = "green"
            elif event.key == pygame.K_b:
                color = "blue"
            elif event.key == pygame.K_e:
                color = "erase"
            elif event.key == pygame.K_c:
                canvas.fill(WHITE)
            elif event.key == pygame.K_1:
                mode = mode_draw
            elif event.key == pygame.K_2:
                mode = mode_circle
            elif event.key == pygame.K_3:
                mode = mode_rect        
        # Mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
            starting_position = event.pos
            last_position = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
            if starting_position and mode in [mode_circle, mode_rect]:
                end_position = event.pos
                rect = pygame.Rect(
                    min(starting_position[0], end_position[0]), 
                    min(starting_position[1], end_position[1]),
                    abs(end_position[0] - starting_position[0]), 
                    abs(end_position[1] - starting_position[1])
                )
                if mode == mode_rect:
                    pygame.draw.rect(canvas, colors[color], rect, 2)
                elif mode == mode_circle:
                    pygame.draw.ellipse(canvas, colors[color], rect, 2)
        elif event.type == pygame.MOUSEMOTION and mouse_down:
            if mode == mode_draw:
                pygame.draw.line(canvas, colors[color],last_position , event.pos, radius * 2)
            last_position = event.pos
    pygame.display.flip()

pygame.quit()
