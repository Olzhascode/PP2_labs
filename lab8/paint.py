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
mode_draw = "Draw"
radius = 10
mode = mode_draw # defualt mode
mouse_down = False
running = True

starting_position = None

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
        
        # Mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False
        elif event.type == pygame.MOUSEMOTION and mouse_down:
            pygame.draw.circle(canvas, colors[color], event.pos, radius)
    pygame.display.flip()

pygame.quit()
