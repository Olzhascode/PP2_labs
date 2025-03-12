import pygame, sys
import datetime
pygame.init()

# Display
width = 800
height = 600
FPS = 60
clock = pygame.time.Clock()
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Mouse clock")

# Images
main_img = pygame.image.load("Mouse.jpg")
main_img = pygame.transform.scale(main_img, (width, height))

right_hand = pygame.image.load("right.png")
left_hand = pygame.image.load("left.png")

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
    # Time
    nowtime = datetime.datetime.now()
    minute = nowtime.minute
    second = nowtime.second

    minute_angle = (minute/60) * 360
    second_angle = (second/60) * 360

    display.fill((255,255, 255))
    display.blit(main_img, (0, 0))
    
    # Calling function
    draw(right_hand, -minute_angle, centerX, centerY, display)
    draw(left_hand, -second_angle, centerX, centerY, display)
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()