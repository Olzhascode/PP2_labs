import pygame

pygame.init()

width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music player")
playlist = ['sounds/The Rolling Stones - Paint It, Black.mp3', 'sounds/Kiss - I Was Made For Lovin You.mp3', 'sounds/The Animals - House Of Rising Sun.mp3', 'sounds/White Town - Your Woman.mp3']
track = 0
pygame.mixer.music.load(playlist[track])

playing = False
paused = False

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    if paused:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                    paused = not paused
                else:
                    pygame.mixer.music.play()
                    playing = True
                    paused = False
            


    display.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()