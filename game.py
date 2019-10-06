import pygame

pygame.init()

window = pygame.display.set_mode((600,600))
pygame.display.set_caption("My First Game")

game_over = False
x = 75
y = 75
r = 75

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
      y -= 15
    if keys[pygame.K_a]:
      x -= 15
    if keys[pygame.K_s]:
      y += 15
    if keys[pygame.K_d]:
      x += 15

    window.fill((255,255,255))
    pygame.draw.circle(window, (0,0,255), (x,y), r)
    pygame.display.flip()

pygame.quit()
