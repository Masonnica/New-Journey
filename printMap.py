import pygame
import math
from setting import *
from block import Block

class Print:
  def __init__(self, pos):
    printTile(x, y)
    
def printTile(x, y, map):
  for a in range(-(blockHeight / 2), (blockHeight / 2) + 1):.
    for b in range(-(blockWidth / 2), (blockWidth / 2) + 1):
      block = Block(id, Tile)
      rect = block.get_rect(topleft = pos)