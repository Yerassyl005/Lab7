import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("music/Tom's Diner.mp3")
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Custom Music Player")

done = False
flPause = False
vol = 5.0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_UP:
                vol += 0.4
                pygame.mixer.music.set_volume(vol)
                print(pygame.mixer.music.get_volume())
            elif event.key == pygame.K_DOWN:
                vol -= 0.4
                pygame.mixer.music.set_volume(vol)
                print(pygame.mixer.music.get_volume())
