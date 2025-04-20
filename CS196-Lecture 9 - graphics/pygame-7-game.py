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
PLAYER_JUMP_VELOCITY = -600
GRAVITY = 800
ENEMY_WIDTH = 100
ENEMY_HEIGHT = 100
ENEMY_SPEEDUP = 1.2

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Define fonts
FONT_INFO = pygame.font.SysFont("Arial", 24)
FONT_LARGE = pygame.font.SysFont ("Arial", 48)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hello World")

# Draw text
def drawText(txt,color,position=(10,10)):
  text_surface = FONT_INFO.render(txt, True, color) # True for antialiasing
  screen.blit(text_surface, position)  # Draw the text onto the screen
def drawTextCenter(txt, color):
  text_surface = FONT_LARGE.render(txt, True, color)  # True for antialiasing
  text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
  screen.blit(text_surface, text_rect)  # Draw the text onto the screen

# Collision detection function
def collision(x1,y1,w1,h1,x2,y2,w2,h2):
  # is x1 left of x2?
  if x1 + w1 < x2: return False
  # is x1 right of x2?
  if x1 > x2 + w2: return False
  # is y1 below y2?
  if y1 + h1 < y2: return False
  # is y1 above y2?
  if y1 > y2 + h2: return False
  # otherwise, they are colliding
  return True

# Variables
playerX = 20
playerY = FLOOR - PLAYER_HEIGHT
playerVelocityX = 0
playerVelocityY = 0
playerIsJumping = False
enemyX = SCREEN_WIDTH // 2 - ENEMY_WIDTH // 2
enemyY = FLOOR - ENEMY_HEIGHT
enemyVelocityX = 200

# Game loop
running = True
playing = True
score = 0
while running:
  # Event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  keys = pygame.key.get_pressed()
  # Clock
  clock.tick(MAX_FPS)
  delta = clock.get_time() / 1000.0
  if playing:
    # Update player
    if keys[pygame.K_LEFT] and playerX > 0:
      playerX -= PLAYER_SPEED_X * delta
    if keys[pygame.K_RIGHT] and playerX < SCREEN_WIDTH - PLAYER_WIDTH:
      playerX += PLAYER_SPEED_X * delta
    if keys[pygame.K_SPACE] and not playerIsJumping:
      playerIsJumping = True
      playerVelocityY = PLAYER_JUMP_VELOCITY
    if playerIsJumping:
      playerVelocityY += GRAVITY * delta
      playerY += playerVelocityY * delta
      if playerY >= FLOOR - PLAYER_HEIGHT:
        playerY = FLOOR - PLAYER_HEIGHT
        playerIsJumping = False
    # Update enemy
    enemyX += enemyVelocityX * delta
    if enemyX < 0 or enemyX > SCREEN_WIDTH - ENEMY_WIDTH:
      enemyVelocityX = -enemyVelocityX
      score += 1
      enemyVelocityX *= ENEMY_SPEEDUP
  # Drawing
  screen.fill(BLACK)
  drawText(f'Score: {score}',WHITE)
  pygame.draw.rect(screen, BLUE, (playerX,playerY,PLAYER_WIDTH,PLAYER_HEIGHT))
  pygame.draw.rect(screen, RED, (enemyX,enemyY,ENEMY_WIDTH,ENEMY_HEIGHT))
  # Collision detection
  if collision(playerX, playerY, PLAYER_WIDTH, PLAYER_HEIGHT, enemyX, enemyY, ENEMY_WIDTH, ENEMY_HEIGHT):
    drawTextCenter('Game Over!', RED)
    playing = False
  # Update the display
  pygame.display.flip()

# Quit Pygame
pygame.quit()