import pygame, sys
import datetime
pygame.init()

# Display
width = 600
height = 600
FPS = 60
clock = pygame.time.Clock()
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Mouse clock")

# Images
main_img = pygame.image.load()
main_img = pygame.transform.scale(main_img, (width, height))

right_hand = pygame.image.load("")
left_hand = pygame.image.load("")

# Coordnates
centerX = width//2
centerY = height//2

# Function to draw hands
def draw(hand, angle, centerX, centerY, display):
    RotatedHand = pygame.transform.rotate(hand, angle)
    HandRect = RotatedHand.get_rect(center = (centerX, centerY))
    display.blit(RotatedHand, HandRect) 


run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




    display.fill((255,255, 255))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()