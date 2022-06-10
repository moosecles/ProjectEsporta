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
font = pygame.font.Font('freesansbold.ttf', 20)

# Loading images, mp3 (venv/props/)
gym_bg = pygame.image.load("props/map.png")
punching_bag = pygame.image.load("props/yoga_mat.png")
deadlift = pygame.image.load("props/deadlift.png")
db_rack = pygame.image.load("props/db_rack.png")
bench_press = pygame.image.load("props/bench_press.png")
tread_mill = pygame.image.load("props/tread_mill.png")
db_button = pygame.image.load("props/db_button.png")
ddl_button = pygame.image.load("props/ddl_button.png")
pb_button = pygame.image.load("props/pb_button.png")
treadmill_button = pygame.image.load("props/treadmill_button.png")
bench_button = pygame.image.load("props/bench_button.png")

click_sound = mixer.Sound('props/Click.mp3')
bg_sound = mixer.Sound('props/bg_music2.mp3')

# GLOBAL VARIABLES
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)  # (do this, every this milliseconds)
clock = pygame.time.Clock()
area = pygame.Rect(100, 150, 200, 124)
punchingbag_mask = pygame.mask.from_surface(pb_button)  # Mask = where the punching bag png is
treadmill_mask = pygame.mask.from_surface(treadmill_button)
db_mask = pygame.mask.from_surface(db_button)
bench_mask = pygame.mask.from_surface(bench_button)
ddl_mask = pygame.mask.from_surface(ddl_button)

def draw():  # MAIN FUNCTION TO PASTE EVERYTHING GUI
    # UPGRADE BUTTONS
    punchingbag_X, punchingbag_Y = 815, 60
    treadmill_X, treadmill_Y = 815, 80
    db_X, db_Y = 815, 100
    bench_X, bench_Y = 815, 120
    ddl_X, ddl_Y = 815, 140
    screen.blit(pb_button, (punchingbag_X, punchingbag_Y))
    screen.blit(treadmill_button, (treadmill_X, treadmill_Y))
    screen.blit(db_button, (db_X, db_Y))
    screen.blit(bench_button, (bench_X, bench_Y))
    screen.blit(ddl_button, (ddl_X, ddl_Y))

    # SET THE LOGO
    icon = pygame.image.load("props/logo.png")
    pygame.display.set_icon(icon)


def showScore():

    scoreX = 780
    scoreY = 500
    score = font.render('Points : %s' % str(player.total_points), True, (255, 255, 255))
    screen.blit(score, (scoreX, scoreY))

def button_clicked(x,y):
    if event.button == 1 and punchingbag_mask.get_at((event.pos[0] - x, event.pos[1] - y)):
        if player.total_points >= 100:  # and the points are more than 100 (which is how much u need to buy one)
            player.punching_bag += 1
            player.total_points -= 100

bg_sound.play()  #sets background music to run
bg_sound.set_volume(.01) #sets the volume of said music

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

    for event in pygame.event.get(): #EVENT CHAIN
        clock.tick(60)
        if event.type == pygame.QUIT:  #PRESSING X EVENT
            running = False

        elif event.type == timer_event: #UPGRADE EVENT TIMER
            player.total_points += player.upgrade_multiplier()

        elif event.type == pygame.MOUSEBUTTONDOWN:  #MOUSE BUTTON IS CLICKED EVENT
            pos = pygame.mouse.get_pos()
            x, y = event.pos  # This is where the mouse is clicked if u want a X Y
            # Detect clicking in our game screen.
            if event.button == 1 and area.collidepoint(pos): #CLICK ON GYM AREA EVENT
                click_sound.play()
                player.add_score()
            else:
                button_clicked(x, y)
    showScore()

pygame.quit()
