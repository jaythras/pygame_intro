import pygame

pygame.init()

window = pygame.display.set_mode((600,600))
pygame.display.set_caption("My First Game")

game_over = False

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    pygame.display.flip()

pygame.quit()