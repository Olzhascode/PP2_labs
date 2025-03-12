import pygame

pygame.init()

width, height = 600, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music player")

#Playlist
playlist = ['sounds/The Rolling Stones - Paint It, Black.mp3', 'sounds/Kiss - I Was Made For Lovin You.mp3', 'sounds/The Animals - House Of Rising Sun.mp3', 'sounds/White Town - Your Woman.mp3']
track = 0
pygame.mixer.music.load(playlist[track])

playing = False
paused = False

cover_images = [
    "images/rolling stones.jpg",
    "images/kiss.jpg",
    "images/the animals.jpg",
    "images/white town.jpg"
]
cover = pygame.image.load(cover_images[track])
cover = pygame.transform.scale(cover, (300, 300))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Control tracks
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
            if event.key == pygame.K_LEFT:
                pygame.mixer.music.stop()
                track = (track + 1) % len(playlist)
                pygame.mixer.music.load(playlist[track])
                pygame.mixer.music.play()

                cover = pygame.image.load(cover_images[track])
                cover = pygame.transform.scale(cover, (300, 300))

            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                track = (track - 1) % len(playlist)
                pygame.mixer.music.load(playlist[track])
                pygame.mixer.music.play()

                cover = pygame.image.load(cover_images[track])
                cover = pygame.transform.scale(cover, (300, 300))
    #Volume control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        volume+=0.1
        pygame.mixer.music.set_volume(volume)
    if keys[pygame.K_DOWN]:
        volume-=0.1
        pygame.mixer.music.set_volume(volume)

    #covers
    display.fill((255, 255, 255))
    display.blit(cover, (150, 100))

    button_color = (100, 100, 100)
    
    
    pygame.draw.circle(display, button_color, (300, 450), 30)  
    if playing and not paused:
        pygame.draw.rect(display, (255, 255, 255), (290, 435, 8, 30))
        pygame.draw.rect(display, (255, 255, 255), (302, 435, 8, 30)) 
    else:
        pygame.draw.polygon(display, (255, 255, 255), [(290, 435), (290, 465), (315, 450)])  

    
    pygame.draw.polygon(display, button_color, [(370, 435), (370, 465), (395, 450)]) 
    pygame.draw.rect(display, button_color, (395, 435, 5, 30))  

    
    pygame.draw.polygon(display, button_color, [(230, 435), (230, 465), (205, 450)])  
    pygame.draw.rect(display, button_color, (200, 435, 5, 30))  

    
    pygame.draw.line(display, button_color, (200, 500), (400, 500), 5)  
    pygame.draw.circle(display, (255, 0, 0), (200 + int(volume * 200), 500), 10)
    
    pygame.display.flip()

pygame.quit()