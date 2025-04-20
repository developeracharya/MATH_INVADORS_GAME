import pygame

pygame.init() # initialize pygame
screen = pygame.display.set_mode( (800, 600) ) # Create a window
pygame.display.set_caption("Hello World") # set the window title

# Game loop
running = True
while running:
  # Event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  # Drawing
  pygame.draw.rect(screen, (0,0,255), (400,300,100,200))
  # Update the display
  pygame.display.flip()

pygame.quit()  # teardown