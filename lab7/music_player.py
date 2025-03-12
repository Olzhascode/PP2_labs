import pygame

pygame.init()

width, height = 600, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music player")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    display.fill((255, 255, 255))
    
    pygame.display.flip()

pygame.quit()