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
mode_erase = "Erase"
radius = 10
mode = mode_draw # defualt mode
mouse_down = False
running = True

while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == event.K_r:
                color = "red" 
            elif event.key == event.K_g:
                color = "green"
            elif event.key == event.K_b:
                color = "blue"
            elif event.key == event.K_e:
                color = "erase"
            
    pygame.display.flip()

pygame.quit()
