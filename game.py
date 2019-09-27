import pygame

pygame.init()

window = pygame.display.set_mode((600,600))
pygame.display.set_caption("My First Game")

game_over = False

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True

    window.fill((255,255,255))
    pygame.draw.circle(window, (0,0,255), (75,75), 75)
    pygame.display.flip()

pygame.quit()