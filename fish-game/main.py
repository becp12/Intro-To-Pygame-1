import pygame, random, sys
from pygame.locals import *
from fish import *

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

color = (52, 216, 235)

fishes = []

def main():
  for i in range(10):
    fishes.append(Fish((width/2, height/2)))
    
  while True:
    clock.tick(60) # sets frame rate
    # any event handling
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
    # sprites are updated
    for fish in fishes:
      fish.update()
    # Background / Sprites are drawn in order of layer
    screen.fill(color)
    for fish in fishes:
      fish.draw(screen)
    
    pygame.display.flip()

if __name__ == "__main__":
  main()