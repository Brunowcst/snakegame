import pygame

width, height = 400, 300
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

square_size = 10
game_speed = 15