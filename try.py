import pygame, os
from Bullet import Bullet
from Invador import Invador

pygame.init() # initialize pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode( (800, 600) ) # Create a window
pygame.display.set_caption("Hello World") # set the window title
MAX_FPS = 60
TIMER_EVENT = pygame.USEREVENT + 1

pygame.time.set_timer(TIMER_EVENT, 3000)


#INVADOR
INVADOR_WIDTH = 100
INVADOR_HEIGHT = 100
NUMBER_OF_INVADORS = 5

# test component
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
IMAGES_FOLDER = os.path.join(THIS_FOLDER, 'images')
INVADOR_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, "invador_pic.png"))
INVADOR_IMAGE = pygame.transform.scale(INVADOR_IMAGE, (INVADOR_WIDTH, INVADOR_HEIGHT))

# Game loop
invador = ""
running = True
count = 0
while running:
  clock.tick(MAX_FPS)
  delta = clock.get_time() / 1000
  # Event handling
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == TIMER_EVENT:
      Invador(screen, INVADOR_IMAGE, delta)
      count += 1
      print(count)
  # Drawing
  # keys = pygame.key.get_pressed()
  
  # if keys[pygame.K_LEFT]:
    
  
  # Update the display
  screen.fill((0, 0 ,0))
  
  # if Bullet.bullets:
  #   ...
  if Invador.invadors_list:
    Invador.move_invadors()
  pygame.display.flip()

pygame.quit()  # teardown