import pygame
from pygame import mixer
from player import Player

# Initialize Pygame

pygame.font.init()
pygame.init()
pygame.mixer.init()

background_colour = (255, 255, 255)
(width, height) = (960, 540)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Project Esporta')

# FONT
font = pygame.font.Font('freesansbold.ttf', 32)

# Loading images, mp3 (venv/props/)
gym_bg = pygame.image.load("props/map.png")
punching_bag = pygame.image.load("props/yoga_mat.png")
deadlift = pygame.image.load("props/deadlift.png")
db_rack = pygame.image.load("props/db_rack.png")
bench_press = pygame.image.load("props/bench_press.png")
tread_mill = pygame.image.load("props/tread_mill.png")
click_sound = mixer.Sound('props/Click.mp3')
bg_sound = mixer.Sound('props/bg_music2.mp3')

# GLOBAL VARIABLES
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)  # (do this, every this milliseconds)
clock = pygame.time.Clock()
area = pygame.Rect(100, 150, 200, 124)
punchingbagMask = pygame.mask.from_surface(punching_bag)  # Mask = where the punching bag png is


def draw():  # MAIN FUNCTION TO PASTE EVERYTHING GUI
    # UPGRADE BUTTONS
    punchingBagX, punchingBagY = 850, 60
    screen.blit(punching_bag, (punchingBagX, punchingBagY))

    # SET THE LOGO
    icon = pygame.image.load("props/logo.png")
    pygame.display.set_icon(icon)


def showScore():

    scoreX = 750
    scoreY = 500
    score = font.render('Points : %s' % str(player.total_points), True, (255, 255, 255))
    screen.blit(score, (scoreX, scoreY))


bg_sound.play()
bg_sound.set_volume(.5)

player = Player()

# Game Running
running = True

while running:

    pygame.display.update()
    # Background Image
    screen.blit(gym_bg, (0, 0))
    area = pygame.Rect(0, 0, 775, 540)
    # Event List
    draw()  # Draws the pngs and stuff onto the screen

    for event in pygame.event.get():
        clock.tick(60)

        if event.type == pygame.QUIT:
            running = False
        elif event.type == timer_event:
            player.total_points += player.upgrade_multiplier()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x, y = event.pos  # This is where the mouse is clicked if u want a X Y

            # Detect clicking in our game screen.
            if event.button == 1 and area.collidepoint(pos):
                click_sound.play()
                player.add_score()
            elif event.button == 1 and punchingbagMask.get_at(
                    (event.pos[0] - x, event.pos[1] - y)):  # If it is at the punching bag png location

                if player.total_points >= 100:  # and the points are more than 100 (which is how much u need to buy one)
                    player.punching_bag += 1
                    player.total_points -= 100
    showScore()

pygame.quit()
