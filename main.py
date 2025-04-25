import pygame, os
from Invador import Invador
from Bullet import Bullet

#set screen constants
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700
MAX_FPS = 60

# initializing pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Math Invadors")

# Game mode
ADDITION = False
SUBTRACTION = False
MULTIPLICATION = False
DIVISION = False
RANDOM = False

# Player
PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200
X_PLAYER = 400
Y_PLAYER = 500
PLAYER_DISPLACEMENT = 300

# bullet
BULLET_WIDTH = 50
BULLET_HEIGHT = 50
BULLET_SPEED = 200
BULLET_COUNT = 25

#INVADOR
INVADOR_WIDTH = 100
INVADOR_HEIGHT = 100

# path
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
IMAGES_FOLDER = os.path.join(THIS_FOLDER, 'images')
PLAYER_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, "rocket_pic.png"))
PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (PLAYER_WIDTH, PLAYER_HEIGHT))
BULLET_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, "bullet_pic.png"))
BULLET_IMAGE = pygame.transform.scale(BULLET_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT))
INVADOR_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, "invador_pic.png"))
INVADOR_IMAGE = pygame.transform.scale(INVADOR_IMAGE, (INVADOR_WIDTH, INVADOR_HEIGHT))

# display
running = True
mode_chosen = False
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # CLOCK
    clock.tick(MAX_FPS)
    delta = clock.get_time() / 1000
    if keys[pygame.K_LEFT] and X_PLAYER > -50 :
        X_PLAYER -= PLAYER_DISPLACEMENT * delta
    elif keys[pygame.K_RIGHT] and X_PLAYER < 760:
        X_PLAYER += PLAYER_DISPLACEMENT * delta
    
    if keys[pygame.K_SPACE] and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        Bullet(screen, X_PLAYER, Y_PLAYER, BULLET_SPEED, BULLET_IMAGE, delta)
        # BULLET_COUNT -= 1
        # if not BULLET_COUNT:
        #     print("BULLET FINISH!")
        #     break
    
    screen.fill((0, 0 ,0))
    if Bullet.BULLETS:
        Bullet.move_bullets()
    screen.blit(PLAYER_IMAGE, (X_PLAYER, Y_PLAYER))
    pygame.display.flip()
        
pygame.quit()