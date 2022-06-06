import pygame
print('hi')
background_colour = (255,255,255)
(width, height) = (960, 540)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Project Esporta')

screen.fill(background_colour)
pygame.display.flip()

running = True
while running:
    print('hi')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()