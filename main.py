import pygame
import upgrade
import os

pygame.font.init()
background_colour = (255, 255, 255)
(width, height) = (960, 540)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Project Esporta')

# FONT
font = pygame.font.Font('freesansbold.ttf', 32)

testX = 750
testY = 500


def show_score (x, y):
    score = font.render('Points : %s' % str(total_points), True, (255, 255, 255))
    screen.blit(score, (testX, testY))

# Loading images (venv/props/)
gym_bg = pygame.image.load("map.png")
yoga_mat = pygame.image.load("yoga_mat.png")
deadlift = pygame.image.load("deadlift.png")
db_rack = pygame.image.load("db_rack.png")
bench_press = pygame.image.load("bench_press.png")
tread_mill = pygame.image.load("tread_mill.png")

icon = pygame.image.load("logo.png")
pygame.display.set_icon(icon)


#GLOBAL VARIABLES
total_points = 0
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)  # (do this, every this milliseconds)
clock = pygame.time.Clock()

# Game Running
running = True


while running:
    pygame.display.update()
    # Background Image
    screen.blit(gym_bg, (0, 0))

    # Event List
    for event in pygame.event.get():
        clock.tick(60)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == timer_event:
            total_points += upgrade.upgradeMultiply()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            total_points += 1
            print(total_points)
    show_score(testX, testY)
pygame.quit()




