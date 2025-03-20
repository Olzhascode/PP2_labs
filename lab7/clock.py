import pygame, sys

pygame.init()

# Display
width = 600
height = 600
FPS = 60
clock = pygame.time.Clock()
display = pygame.display.set_mode((width, height))

run = True
while run:
    display.fill((255,255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()