import pygame
import random

pygame.init()
pygame.display.set_caption("Snake game")
width, height = 600, 400
pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

square_size = 10
snake_speed = 15