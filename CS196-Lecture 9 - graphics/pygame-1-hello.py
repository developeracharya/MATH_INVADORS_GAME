import pygame

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

# Set screen constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAX_FPS = 60

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hello World")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Define fonts
FONT_INFO = pygame.font.SysFont("Arial", 24)

# Draw text
def drawText(txt,color,position=(10,10)):
  text_surface = FONT_INFO.render(txt, True, color) # True for antialiasing
  screen.blit(text_surface, position)  # Draw the text onto the screen

# Game loop
running = True
while running:
  # Event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  # Drawing
  drawText(f'Hello world',WHITE)
  pygame.draw.rect(screen, BLUE, (400,300,100,200))
  # Update the display
  pygame.display.flip()
  

# Quit Pygame
pygame.quit()