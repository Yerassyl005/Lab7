import pygame

pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("MickeyClock by RC")
icon = pygame.image.load('images/RC.png')
pygame.display.set_icon(icon)

square = pygame.Surface((70, 70))
square.fill("orange")

myfont = pygame.font.Font("fonts/BadScript-Regular.ttf", 50)
text_surface = myfont.render("Rockstar Games Presents", True, "white")

cpt = pygame.image.load("images/RC.png")

done = False

while not done:
    screen.blit(square, (0, 0))
    pygame.draw.circle(square, "black", (35, 35), 20)
    screen.blit(text_surface, (120, 200))
    #screen.blit(cpt, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
