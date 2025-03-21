import pygame

pygame.init()

width, height = 600, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music player")
playlist = ['sounds/The Rolling Stones - Paint It, Black.mp3', 'sounds/Kiss - I Was Made For Lovin You.mp3', 'sounds/The Animals - House Of Rising Sun.mp3', 'sounds/White Town - Your Woman.mp3']
track = 0
pygame.mixer.music.load(playlist[track])
volume = 0.5

cover_images = [
    "images/rolling stones.jpg",
    "images/kiss.jpg",
    "images/the animals.jpg",
    "images/white town.jpg"
]

cover = pygame.image.load(cover_images[track])
cover = pygame.transform.scale(cover, (300, 300))

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



    #volume
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        volume+=0.1
        pygame.mixer.music.set_volume(volume)
    if keys[pygame.K_DOWN]:
        volume-=0.1
        pygame.mixer.music.set_volume(volume)



    #display.fill()
    display.blit(cover, (150, 100))
    pygame.display.flip()

pygame.quit()