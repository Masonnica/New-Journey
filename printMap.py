import pygame
import math
from settings import *
from block import Block

with open("playPos.txt", "r") as fileOut:
  file = fileOut.readlines()
  file = str(file)
  file = file.replace("\\n", "")
  file = file.replace("'", "")
  file = file.replace("[", "")
  file = file.replace("]", "")
  file = file.split(",")
  x = file[0]
  y = file[1]
  z = file[2]

def print(x = x, y = y, z = z):
  printTile(x, y, z)
    
def printTile(x, y, z, map):
  if z > 5:
    re = 6
  else:
    re = z + 1
  for a in range(0, re):
    for b in range(-(blockHeight / 2), (blockHeight / 2) + 1):
      for c in range(-(blockWidth / 2), (blockWidth / 2) + 1):
        pos = ((Width / 2), (Height / 2))
        block = Block(id, "Tile")
        rect = block.get_rect(topleft = pos)