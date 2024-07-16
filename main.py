import pygame, random, sys
from pygame.locals import *

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

color = (52, 216, 235)
fish_image = pygame.image.load("fish.png")
fish_image = pygame.transform.smoothscale(fish_image, (80, 80))
fish_rect = fish_image.get_rect()
fish_rect.center = (width//2, height//2)

speed = pygame.math.Vector2(0, 10)
rotation = random.randint(0, 360)
speed.rotate_ip(rotation)
fish_image = pygame.transform.rotate(fish_image, 180-rotation)

def move_fish():
  global fish_image
  screen_info = pygame.display.Info()

  fish_rect.move_ip(speed)
  
  if fish_rect.left < 0 or fish_rect.right > screen_info.current_w:
    speed[0] *= -1
    fish_image = pygame.transform.flip(fish_image, True, False)
    fish_rect.move_ip(speed[0], 0)

  if fish_rect.top < 0 or fish_rect.bottom > screen_info.current_h:
    speed[1] *= -1
    fish_image = pygame.transform.flip(fish_image, False, True)
    fish_rect.move_ip(0, speed[1])
    
  

def main():
  while True:
    clock.tick(60) # sets frame rate
    # any event handling
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_d:
          print("I pressed the d key")
        elif event.key == K_c:
          print("I pressed the c key")
      if event.type == MOUSEBUTTONDOWN:
        print("I clicked the mouse")
    # sprites are updated
    move_fish()
    # Background / Sprites are drawn in order of layer
    screen.fill(color)
    screen.blit(fish_image, fish_rect)
    pygame.display.flip()

if __name__ == "__main__":
  main()