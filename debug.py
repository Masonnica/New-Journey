import pygame

pygame.init()
font = pygame.font.Font(None, 26)

def debug(info, x = 2, y = 2):
  display_surface = pygame.display.get_surface()
  debug_surf = font.render(str(info), True, 'White')
  debug_rect = debug_surf.get_rect(topleft = (x, y))
  pygame.draw.rect(display_surface, 'Black', debug_rect)
  display_surface.blit(debug_surf, debug_rect)