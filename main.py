import pygame, sys
from pygame.locals import *
from settings import *
from menu import *
from printMap import *
from debug import debug

class Game:
  def __init__(self):
    pygame.init()
    pygame_icon = pygame.image.load("png/UI/logo.png")
    pygame.display.set_icon(pygame_icon)
    pygame.display.set_caption("New Journey" + Version)
    self.screen = pygame.display.set_mode((Width, Height))
    self.clock = pygame.time.Clock()

  def run(self):
    print(menuHome())
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
          return 0

      self.screen.fill('white')
      self.clock.tick(FPS)
      pygame.display.update()

if __name__ == '__main__':
  game = Game()
  game.run()