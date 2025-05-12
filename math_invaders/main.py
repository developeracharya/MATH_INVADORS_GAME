import pygame, os
from Invador import Invador
from Bullet import Bullet
from Button import Button
import json
import random
#set screen constants
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700

# BUTTON 
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50


# initializing pygame
pygame.init()
pygame.mixer.init() 
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Math Invadors")

#speaker width
SPEAKER_WIDTH = 30
SPEAKER_HEIGHT = 30
SPEAKER_X = 850
SPEAKER_Y = 5
SPEAKER_ON = True

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# TIME OUT SET
MAX_FPS = 60
TIMER_EVENT = pygame.USEREVENT + 1

pygame.time.set_timer(TIMER_EVENT, 1000)

#music 
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
SOUND_FOLDER = os.path.join(THIS_FOLDER, 'sounds')
BACKGROUND_MUSIC = pygame.mixer.music.load(os.path.join(SOUND_FOLDER, "song21.mp3"))
LASER_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, "laser1.ogg"))
EXPLOSION_SOUND = pygame.mixer.Sound(os.path.join(SOUND_FOLDER, "explosion2.ogg"))

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
PLAYER_HEALTH = 5
X_PLAYER = 400
Y_PLAYER = 500
PLAYER_DISPLACEMENT = 3000
SCORE = 0

# bullet
BULLET_WIDTH = 50
BULLET_HEIGHT = 50
BULLET_SPEED = 200
BULLET_COUNT = 25
WRONG_COLLISION = False

#running 
running = True

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
BACKGROUND_IMAGE= pygame.image.load(os.path.join(IMAGES_FOLDER, "back_ground.png"))
BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, (WINDOW_WIDTH, WINDOW_HEIGHT))
SPEAKER_ON_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, "speaker_on.png"))
SPEAKER_ON_IMAGE = pygame.transform.scale(SPEAKER_ON_IMAGE, (SPEAKER_WIDTH, SPEAKER_HEIGHT))
SPEAKER_OFF_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, "speaker_off.png"))
SPEAKER_OFF_IMAGE = pygame.transform.scale(SPEAKER_OFF_IMAGE, (SPEAKER_WIDTH, SPEAKER_HEIGHT))

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
    

DATA_FILE = os.path.join(THIS_FOLDER, 'data.json')
HIGH_SCORE = 0

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as file:
        try:
            data = json.load(file)
            HIGH_SCORE = data.get("high_score", 0)
        except json.JSONDecodeError:
            HIGH_SCORE = 0
else:
    with open(DATA_FILE, 'w') as file:
        json.dump({"high_score": 0}, file)
        
#QUESTION INVADOR
question_invador = ""
pygame.mixer.music.play(-1)
start_game = False
while not start_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(pygame.mouse.get_pos()) 
            # print(pygame.mouse.get_pos(), Button.button_click(pygame.mouse.get_pos()))
            if Button.button_click(pygame.mouse.get_pos()) == "start-game-btn":
                running = True
                start_game = True
                break
            
            elif Button.button_click(pygame.mouse.get_pos()) == "end-game-btn":
                running = False
                print("game ended")
                start_game = True
                break
            
            elif Button.button_click(pygame.mouse.get_pos()) == "speaker":
                print("this is speaker", SPEAKER_ON)
                SPEAKER_ON = not SPEAKER_ON
                if SPEAKER_ON:
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.stop()
                print(SPEAKER_ON)
    #   screen.fill((0, 0, 0))

    screen.blit(BACKGROUND_IMAGE, (0, 0))
    Button("speaker",screen, "", SPEAKER_WIDTH, SPEAKER_HEIGHT, (SPEAKER_X, SPEAKER_Y), (0, 0, 0), (0, 0, 0), speaker=True, on=SPEAKER_ON, speaker_pic = (SPEAKER_ON_IMAGE, SPEAKER_OFF_IMAGE))
    Button("start-game-btn",screen, "Start Game", BUTTON_WIDTH, BUTTON_HEIGHT, (WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 - 100), (255, 255, 255), (255, 0, 0))
    Button("end-game-btn",screen, "Quit", BUTTON_WIDTH, BUTTON_HEIGHT, (WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2), (255, 0, 0),(255,255, 255))
    pygame.display.flip()
    

# display

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == TIMER_EVENT and len(Invador.alive_invadors) <= 5:
            invador_created = True
            while invador_created:
                new_invador = Invador(screen, INVADOR_IMAGE, delta, random.choice(MODE))
                if Invador.value_checker(new_invador) and len(Invador.alive_invadors) > 1:
                    continue
                else: 
                    Invador.invadors_list.append(new_invador)
                    Invador.alive_invadors.append(new_invador)  
                    break
                    
    
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
            if SPEAKER_ON:
                pygame.mixer.Sound.play(LASER_SOUND)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Button.button_click(pygame.mouse.get_pos()) == "start-game-btn":
                running = True
                PLAYER_HEALTH = 5
                SCORE = 0
                Invador.alive_invadors = []
                Invador.dead_invadors = []
                Invador.invadors_list = []
                question_invador = None
            elif Button.button_click(pygame.mouse.get_pos()) == "end-game-btn":
                running = False
                print("game ended")
                start_game = True
                break
            
            elif Button.button_click(pygame.mouse.get_pos()) == "speaker":
                print("this is speaker", SPEAKER_ON)
                SPEAKER_ON = not SPEAKER_ON
                if SPEAKER_ON:
                    pygame.mixer.music.play(-1)
                else:
                    pygame.mixer.music.stop()
                print(SPEAKER_ON)
        # BULLET_COUNT -= 1
        # if not BULLET_COUNT:
        #     print("BULLET FINISH!")
        #     break
    
    screen.blit(BACKGROUND_IMAGE, (0, 0))
    Button("speaker",screen, "", SPEAKER_WIDTH, SPEAKER_HEIGHT, (SPEAKER_X, SPEAKER_Y), (0, 0, 0), (0, 0, 0), speaker=True, on=SPEAKER_ON, speaker_pic = (SPEAKER_ON_IMAGE, SPEAKER_OFF_IMAGE))
    if question_invador:
        drawTextCenter(display_text, WHITE)
        
    if Invador.invadors_list:
        Invador.move_invadors()


    if Bullet.BULLETS:
        invador_colloided = Bullet.move_bullets()
        if invador_colloided == question_invador:
            SCORE += 1
            if SPEAKER_ON:
                pygame.mixer.Sound.play(EXPLOSION_SOUND)
            Invador.dead_invadors.append(invador_colloided)
            Invador.alive_invadors.remove(invador_colloided)
            Invador.increase_speed()
            question_invador = ""
        elif invador_colloided:
            PLAYER_HEALTH -= 1
        
    if not PLAYER_HEALTH:
        if SCORE > HIGH_SCORE:
            HIGH_SCORE = SCORE
            with open(DATA_FILE, 'w') as file:
                json.dump({"high_score": HIGH_SCORE}, file)
                
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        drawText(txt=f"Your Score: {SCORE}", color=RED, position=(WINDOW_HEIGHT//2, WINDOW_WIDTH//2 - 50))
        drawTextCenter("Invadors Killed You!", (0, 200, 0))
        Button("start-game-btn",screen, "Start Game", BUTTON_WIDTH, BUTTON_HEIGHT, (WINDOW_WIDTH//2 - 250, WINDOW_HEIGHT//2 + 100), (255, 255, 255), (255, 0, 0))
        Button("end-game-btn",screen, "Quit", BUTTON_WIDTH, BUTTON_HEIGHT, (WINDOW_WIDTH//2 , WINDOW_HEIGHT//2 + 100), (255, 0, 0),(255,255, 255))
    
    if SCORE == 25:
        if SCORE > HIGH_SCORE:
            HIGH_SCORE = SCORE
            with open(DATA_FILE, 'w') as file:
                json.dump({"high_score": HIGH_SCORE}, file)
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        drawText(txt=f"Your Score: {SCORE}", color=RED, position=(WINDOW_HEIGHT//2, WINDOW_WIDTH//2 - 50))
        drawTextCenter("You won the invadors!", (0, 200, 0))
        Button("start-game-btn",screen, "Start Game", BUTTON_WIDTH, BUTTON_HEIGHT, (WINDOW_WIDTH//2 - 250, WINDOW_HEIGHT//2 + 100), (255, 255, 255), (255, 0, 0))
        Button("end-game-btn",screen, "Quit", BUTTON_WIDTH, BUTTON_HEIGHT, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100), (255, 0, 0),(255,255, 255))
    else:
        drawText(txt=f"Your Score: {SCORE}", color="Yellow", position=(700, 50), size=12)
        drawText(txt=f"Your Health: {PLAYER_HEALTH}", color="Yellow", position=(800, 50), size=12)
        drawText(txt=f"High Score: {HIGH_SCORE}", color="Yellow", position=(700, 70), size=12)
    screen.blit(PLAYER_IMAGE, (X_PLAYER, Y_PLAYER))
    pygame.display.flip()
    
pygame.quit()