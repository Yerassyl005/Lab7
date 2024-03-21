import pygame
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

font = pygame.font.SysFont('Verdana', 200)

done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # set background
    screen.fill(pygame.Color('black'))
    # get time
    t = datetime.now()
    # draw clock
    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('forestgreen'), pygame.Color('orange'))
    screen.blit(time_render, (120, 150))

    pygame.display.flip()
    clock.tick(20)