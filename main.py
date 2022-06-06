import pygame
import os

background_colour = (255, 255, 255)
(width, height) = (960, 540)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Project Esporta')

# Loading images
gym_bg = pygame.image.load("venv/props/gym_background.png")
yoga_mat = pygame.image.load("venv/props/yoga_mat.png")
deadlift = pygame.image.load("venv/props/deadlift.png")
db_rack = pygame.image.load("venv/props/db_rack.png")
bench_press = pygame.image.load("venv/props/bench_press.png")
tread_mill = pygame.image.load("venv/props/tread_mill.png")

# icon = pygame.image.load(IMAGE_NAME)
# pygame.display.set_icon(icon)



# Game Running
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pointTimer = pygame.time.Clock()
pointTimer.tick(30)

pygame.display.update()
# Background Image
screen.blit(gym_bg, (0, 0))
pygame.quit()