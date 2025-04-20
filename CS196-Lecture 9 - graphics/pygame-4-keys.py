import pygame

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Set screen constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAX_FPS = 60

# Game constants
FLOOR = SCREEN_HEIGHT - 50
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 200
PLAYER_SPEED_X = 200

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Define fonts
FONT_INFO = pygame.font.SysFont("Arial", 24)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hello World")

# Draw text
def drawText(txt,color,position=(10,10)):
  text_surface = FONT_INFO.render(txt, True, color) # True for antialiasing
  screen.blit(text_surface, position)  # Draw the text onto the screen

# Variables
playerX = 20
playerY = FLOOR - PLAYER_HEIGHT
playerVelocityX = 0

# Game loop
running = True
while running:
  # Event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  keys = pygame.key.get_pressed()
  # Clock
  clock.tick(MAX_FPS)
  delta = clock.get_time() / 1000.0
  # Update
  if keys[pygame.K_LEFT]:
    playerX -= PLAYER_SPEED_X * delta
  if keys[pygame.K_RIGHT]:
    playerX += PLAYER_SPEED_X * delta
  # Drawing
  screen.fill(BLACK)
  drawText(f'Hello world.  FPS: {int(1/delta)}',WHITE)
  pygame.draw.rect(screen, BLUE, (playerX,playerY,PLAYER_WIDTH,PLAYER_HEIGHT))
  # Update the display
  pygame.display.flip()
  

# Quit Pygame
pygame.quit()