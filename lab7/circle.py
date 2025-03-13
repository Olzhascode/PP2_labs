import pygame, sys
from pygame.locals import *

pygame.init()

# Display
height = 600
width = 800
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Circle")

# circle coordinates
x = 400
y = 300
radius = 25

#FPS
FPS = 144
clock = pygame.time.Clock()

# Main cycle
run = True
while run:
    display.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= 20
    if keys[pygame.K_DOWN]:
        y += 20
    if keys[pygame.K_LEFT]:
        x -= 20
    if keys[pygame.K_RIGHT]:
        x += 20
    


    # Borders
    if y - radius < 0:
        y = radius
    elif y + radius > height:
        y = height - radius
    elif x - radius < 0:
        x = radius
    elif x + radius > width:
        x = width - radius
    # Circle
    pygame.draw.circle(display, (255, 0, 0), (x, y), radius)
    #
    pygame.display.flip()

    clock.tick(FPS)
pygame.quit()
sys.exit()
