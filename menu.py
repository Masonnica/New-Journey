import pygame
import math
from settings import *

pygame.init()
font = pygame.font.Font(None, 26)

def menuHome():
  surface = pygame.display.get_surface()
  
  mouseX, mouseY = pygame.mouse.get_pos()

  pygame.draw.rect(surface, 'gray', ((Width / 2) - 100, 40, 200, 30))
  pygame.draw.rect(surface, 'gray', ((Width / 2) - 100, 80, 200, 30))
  pygame.draw.rect(surface, 'gray', ((Width / 2) - 100, 120, 200, 30))

  text1 = font.render('PLAY', True, 'White')
  text2 = font.render('LOAD GAME', True, 'White')
  text3 = font.render('SETTING', True, 'White')
    
  surface.blit(text1, ((Width / 2) - 100, 40))
  surface.blit(text2, ((Width / 2) - 100, 80))
  surface.blit(text3, ((Width / 2) - 100, 120))
    
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:
        if mouseX >= (Width / 2) - 100 and mouseX <= (Width / 2) + 100:
          if mouseY >= 40 and mouseY <= 40 + 30:
            return 1
          elif mouseY >= 80 and mouseY <= 80 + 30:
            return 2
          elif mouseY >= 120 and mouseY <= 120 + 30:
            return 3
