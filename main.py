import pygame
from pygame import mixer
from player import Player

pygame.font.init()
pygame.init()
background_colour = (255, 255, 255)
(width, height) = (960, 540)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Project Esporta')

# FONT
font = pygame.font.Font('freesansbold.ttf', 32)

# GYM BG AREA
area = pygame.Rect(100, 150, 200, 124)

scoreX = 750
scoreY = 500

# Loading images, mp3 (venv/props/)
gym_bg = pygame.image.load("props/map.png")
punching_bag = pygame.image.load("props/yoga_mat.png")
deadlift = pygame.image.load("props/deadlift.png")
db_rack = pygame.image.load("props/db_rack.png")
bench_press = pygame.image.load("props/bench_press.png")
tread_mill = pygame.image.load("props/tread_mill.png")
click_sound = mixer.Sound('props/Click.mp3')

icon = pygame.image.load("props/logo.png")
pygame.display.set_icon(icon)

# GLOBAL VARIABLES
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)  # (do this, every this milliseconds)
clock = pygame.time.Clock()

# Game Running

player = Player()


def show_score(x, y):
    score = font.render('Points : %s' % str(player.total_points), True, (255, 255, 255))
    screen.blit(score, (scoreX, scoreY))

# Game Running
running = True
while running:
    pygame.display.update()

    # Background Image
    screen.blit(gym_bg, (0, 0))

    # Upgrade Buttons
    screen.blit(punching_bag, (850, 60))
    area = pygame.Rect(0, 0, 775, 540)
    # Event List
    for event in pygame.event.get():
        clock.tick(60)
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == timer_event:
        # player.total_points += 1

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if event.button == 1 and area.collidepoint(pos):
                click_sound.play()
                player.add_score()

    show_score(scoreX, scoreY)
pygame.quit()
