import pygame
import random

pygame.init()
pygame.display.set_caption("Snake game")
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

def generate_food():
    food_x = round(random.randrange(0, width - square_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - square_size) / 10.0) * 10.0

    return food_x, food_y

def draw_food(size, food_x, food_y):
    pygame.draw.rect(screen, blue, [food_x, food_y, size, size])

def draw_snake(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, white, [pixel[0], pixel[1], size, size])

def draw_score(score):
    font = pygame.font.SysFont("Helvetica", 15)
    text = font.render(f"Score: {score}", True, green)
    screen.blit(text, [1, 1])

def exec_game():
    end_game = False

    x = width / 2
    y = height / 2

    speed_x = 0
    speed_y = 0

    snake_size = 1
    pixels = []

    food_x, food_y = generate_food()

    while not end_game:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
        
        draw_food(square_size, food_x, food_y)

        # draw snake
        pixels.append([x, y])

        if len(pixels) > snake_size:
            del pixels[0]

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                end_game = True

        draw_snake(square_size, pixels)

        draw_score(snake_size - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            snake_size += 1
            food_y, food_y = generate_food()
        clock.tick(game_speed)

exec_game()