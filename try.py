import pygame, os
from Bullet import Bullet
from Invador import Invador
from Button import Button

#set screen constants
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700

# BUTTON 
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50


pygame.init() # initialize pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) ) # Create a window
pygame.display.set_caption("Hello World") # set the window title
MAX_FPS = 60
TIMER_EVENT = pygame.USEREVENT + 1

pygame.time.set_timer(TIMER_EVENT, 3000)

# test component
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
IMAGES_FOLDER = os.path.join(THIS_FOLDER, 'images')

# Game loop
invador = ""
running = True
count = 0
i=0

while running:
  clock.tick(MAX_FPS)
  delta = clock.get_time() / 1000
  # Event handling
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    # if event.type == pygame.MOUSEBUTTONDOWN:
    #   # print(pygame.mouse.get_pos()) 
    #   print(Button.button_click(pygame.mouse.get_pos()))
    #   if Button.button_click(pygame.mouse.get_pos()) == "start-game-btn":
    #     running = True
    #   elif Button.button_click(pygame.mouse.get_pos()) == "end-game-btn":
    #     running = False
    #     print("game ended")
  # Update the display
  # screen.fill((0, 0 ,0))
  # Button("start-game-btn",screen, "Start Game", BUTTON_WIDTH, BUTTON_HEIGHT, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), (255, 255, 255))
  # Button("end-game-btn",screen, "Quit", BUTTON_WIDTH, BUTTON_HEIGHT, (WINDOW_WIDTH//2 + 200, WINDOW_HEIGHT//2+200), (255, 0, 0))
  # print(button.props)
  # print("running", i)
  # if Bullet.bullets:
  #   ...
  # if Invador.invadors_list:
  #   Invador.move_invadors()
  pygame.display.flip()

pygame.quit()  # teardown