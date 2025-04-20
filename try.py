import pygame, os
from Bullet import Bullet
pygame.init() # initialize pygame
screen = pygame.display.set_mode( (800, 600) ) # Create a window
pygame.display.set_caption("Hello World") # set the window title
# bullet
BULLET_WIDTH = 50
BULLET_HEIGHT = 100
X_BULLET = 400
Y_BULLET = 550
BULLET_SPEED = 1

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
IMAGES_FOLDER = os.path.join(THIS_FOLDER, 'images')
BULLET_IMAGE = pygame.image.load(os.path.join(IMAGES_FOLDER, "bullet_pic.png"))
BULLET_IMAGE = pygame.transform.scale(BULLET_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT))
# Game loop
running = True
while running:
  # Event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  # Drawing
  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE]:
    Bullet(screen, X_BULLET, Y_BULLET, BULLET_SPEED, BULLET_IMAGE)
    
  
  # Update the display
  screen.fill((0, 0 ,0))
  
  if Bullet.bullets:
    Bullet.move_bullets()
    
  pygame.display.flip()

pygame.quit()  # teardown