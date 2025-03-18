import pygame, sys
from pygame.locals import *

pygame.init()

height = 800
width = 600


display = pygame.display.set_mode((height, width))
pygame.display.set_caption("Circle")
run = True
display.fill((255, 255, 255))
x = 400
y = 300

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= 20
            if event.key == pygame.K_DOWN:
                y += 20    
    pygame.draw.circle(display, (255, 0, 0), (x, y), 25)
    pygame.display.update()



