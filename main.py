import pygame, os
from Invador import Invador
from Bullet import Bullet
import random
#set screen constants
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700


# initializing pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Math Invadors")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# TIME OUT SET
MAX_FPS = 60
TIMER_EVENT = pygame.USEREVENT + 1

pygame.time.set_timer(TIMER_EVENT, 1000)

# Game mode
ADDITION = False
SUBTRACTION = False
MULTIPLICATION = False
DIVISION = False
RANDOM = False
MODE = ["addition", "subtraction", "multiplication", "division"]

# Player
PLAYER_WIDTH = 200
PLAYER_HEIGHT = 200
X_PLAYER = 400
Y_PLAYER = 500
PLAYER_DISPLACEMENT = 3000
SCORE = 0

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


# Define fonts
# FONT_INFO = pygame.font.SysFont("Arial", 24)
FONT_LARGE = pygame.font.SysFont ("Arial", 48)

#TEXT DRAWER

def drawTextCenter(txt, color):
  text_surface = FONT_LARGE.render(txt, True, color)  # True for antialiasing
  text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
  screen.blit(text_surface, text_rect)  # Draw the text onto the screen

def drawText(txt,color,size= 24, position=(10,10)):
        text_surface = pygame.font.SysFont("Arial", size).render(txt, True, color) # True for antialiasing
        screen.blit(text_surface, position)  # Draw the text onto the screen
    

#QUESTION INVADOR
question_invador = ""

# display
running = True
mode_chosen = False
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TIMER_EVENT and len(Invador.alive_invadors) <= 5:
            Invador(screen, INVADOR_IMAGE, delta, random.choice(MODE))
    
    if not question_invador and Invador.alive_invadors:
        question_invador = Invador.random_invador()
        display_text = f"{question_invador.value_fun(question_invador.mode)}"

    # CLOCK
    clock.tick(MAX_FPS)
    delta = clock.get_time() / 1000
      
    for event in pygame.event.get():
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
    
    if question_invador:
        drawTextCenter(display_text, WHITE)
        
    if Invador.invadors_list:
        Invador.move_invadors()


    if Bullet.BULLETS:
        invador_colloided = Bullet.move_bullets()
        if invador_colloided == question_invador:
            SCORE += 1
            Invador.dead_invadors.append(invador_colloided)
            Invador.alive_invadors.remove(invador_colloided)
            question_invador = ""
    if SCORE == 5:
        screen.fill((0, 0 ,0))
        drawText(txt=f"Your Score: {SCORE}", color=RED, position=(WINDOW_HEIGHT//2, WINDOW_WIDTH//2 - 50))
        drawTextCenter("You won the invadors!", (0, 200, 0))
    else:
        drawText(txt=f"Your Score: {SCORE}", color="Yellow", position=(WINDOW_HEIGHT//2, WINDOW_WIDTH//2 - 70), size=12)
    screen.blit(PLAYER_IMAGE, (X_PLAYER, Y_PLAYER))
    pygame.display.flip()
    
pygame.quit()