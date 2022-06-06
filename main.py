import pygame
import os

background_colour = (255, 255, 255)
(width, height) = (960, 540)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Project Esporta')

# Loading images (venv/props/)
gym_bg = pygame.image.load("gym_background.png")
yoga_mat = pygame.image.load("yoga_mat.png")
deadlift = pygame.image.load("deadlift.png")
db_rack = pygame.image.load("db_rack.png")
bench_press = pygame.image.load("bench_press.png")
tread_mill = pygame.image.load("tread_mill.png")

# icon = pygame.image.load(IMAGE_NAME)
# pygame.display.set_icon(icon)


#GLOBAL VARIABLES
total_points = 0


# Game Running
running = True

while running:
    pygame.display.update()
    # Background Image
    screen.blit(gym_bg, (0, 0))

    pointTimer = pygame.time.Clock()
    pointTimer.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Points System
    def tickingClock(total_points):
        total_points += 1
    pygame.time.set_timer(tickingClock(total_points), 1000)  # periodically do this.
    print(str(total_points))

pygame.quit()




