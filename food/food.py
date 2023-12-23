import random
import pygame
from configs.configs import width, square_size, height, screen, blue

def generate_food(pixels):
    while True:
        food_x = round(random.randrange(0, width - square_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - square_size) / 10.0) * 10.0

        # Verifica se a comida não está na posição da cobra
        if [food_x, food_y] not in pixels:
            return food_x, food_y

def draw_food(size, food_x, food_y):
    pygame.draw.rect(screen, blue, [food_x, food_y, size, size])