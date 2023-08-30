import pygame

def Block(id, type):
  if type == "Tile":
    Tile(id)

def Tile(id):
  tile = ['Unknown',
          'Grass',
          'Dirt',
          'Water',
          'Road Stone',
          'Road',
          'RoadMaker_X(White)',
          'RoadMaker_Y(White)',
          'RoadMaker_N(White)',
          'RoadMaker_E(White)',
          'RoadMaker_S(White)',
          'RoadMaker_W(White)',
          'RoadMaker_X(Yellow)',
          'RoadMaker_Y(Yellow)',
          'RoadMaker_N(Yellow)',
          'RoadMaker_E(Yellow)',
          'RoadMaker_S(Yellow)',
          'RoadMaker_W(Yellow)',
          'Plow_X(Dirt)',
          'Plow_Y(Dirt)',
          'Plow_X(Grass)',
          'Plow_Y(Grass)'
          ]
  return pygame.image.load("png/Tile/" + tile[id] + ".png")

