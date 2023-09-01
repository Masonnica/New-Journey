import pygame
import math
from settings import *

pygame.init()

screen = pygame.display.set_mode((Width, Height))

def menuHome():
  while True:

    mouseX, mouseY = pygame.mouse.get_pos()

    pygame.draw.rect(screen, 'black', ((Width / 2) - 100, 40, 200, 30))
    pygame.draw.rect(screen, 'black', ((Width / 2) - 100, 80, 200, 30))
    pygame.draw.rect(screen, 'black', ((Width / 2) - 100, 120, 200, 30))
    
    screen.blit('PLAY', ((Width / 2) - 100, 40))
    screen.blit('LOAD GAME', ((Width / 2) - 100, 80))
    screen.blit('SETTING', ((Width / 2) - 100, 120))
    
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if mouseX >= (Width / 2) - 100 and mouseX <= (Width / 2) + 100:
            if mouseY >= 40 and mouseY <= 40 + 30:
              command = 1
            elif mouseY >= 80 and mouseY <= 80 + 30:
              command = 2
            elif mouseY >= 120 and mouseY <= 120 + 30:
              command = 3
          return command