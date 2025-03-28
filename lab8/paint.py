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

# Canvas
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(WHITE)

running = True

while running:
    screen.fill(WHITE)
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
