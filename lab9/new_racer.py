import pygame, sys
from pygame.locals import *
import random, time
 
#Initializing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
N = 10
 
#Create a screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

#Score
score = 0
f2 = pygame.font.Font(None, 24)

#GAME OVER text
f = pygame.font.Font(None, 56)
text = f.render("Game Over", 1, (0, 0, 0))
text_rect = text.get_rect(center=(200, 300))

#Enemy model
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Car2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)    
 
      def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
#Player model
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/Car1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(10, 0)
 
#Coin model
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("images/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)    
        self.value = random.randint(1, 5)
 
      def move(self):
        self.rect.move_ip(0,SPEED//2)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
            self.value = random.randint(1, 5)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
#Background
background = pygame.image.load("images/Background.png")

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
    
    DISPLAYSURF.blit(background, (0, 0))

    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    #DISPLAYSURF.fill(WHITE)
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    #Score
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
        score += coin.value
        newcoin = Coin()
        coins.add(newcoin)
        all_sprites.add(newcoin)
    
    # Increase speed every new 10 points
    if score >= N:
        SPEED += 0.5
        N += 10
    score_text = f2.render(f"Your Score: {score}", True, BLACK) 
    DISPLAYSURF.blit(score_text, (10, 10))

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          
          DISPLAYSURF.blit(text, text_rect)
          DISPLAYSURF.blit(score_text, (200, 320))
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(3)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)