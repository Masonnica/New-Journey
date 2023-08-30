import pygame, sys
from pygame.locals import *
from settings import *
from printMap import *
from debug import debug

class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption("New Journey")
    self.screen = pygame.display.set_mode((Width, Hight))
    self.clock = pygame.time.Clock()

  def run(self):
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()

      self.screen.fill('white')
      self.clock.tick(FPS)
      pygame.display.update()

if __name__ == '__main__':
  game = Game()
  game.run()