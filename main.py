import sys
import pygame

from configs.configs import *
from snake.snake import draw_snake
from messages.messages import draw_pause_message, draw_score, game_over_dialog
from food.food import draw_food, generate_food
from controls.controls import select_speed

pygame.init()
pygame.display.set_caption("Snake game")

def exec_game():
    end_game = False
    game_paused = False

    x = width / 2
    y = height / 2

    speed_x = 0
    speed_y = 0

    snake_size = 1
    pixels = []

    food_x, food_y = generate_food(pixels)

    while not end_game:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p or event.key == pygame.K_SPACE:
                    game_paused = not game_paused
                elif game_paused:
                    game_paused = False
                else:
                    speed_x, speed_y = select_speed(event.key, (speed_x, speed_y))
                    
        if not game_paused:
            draw_food(square_size, food_x, food_y)

            if x < 0 or x >= width or y < 0 or y >= height:
                if game_over_dialog():
                        x = width / 2
                        y = height / 2
                        speed_x = 0
                        speed_y = 0
                        snake_size = 1
                        pixels = []
                        food_x, food_y = generate_food(pixels)
                else:
                    pygame.quit()
                    sys.exit()

            x += speed_x
            y += speed_y

            # draw snake
            pixels.append([x, y])

            if len(pixels) > snake_size:
                del pixels[0]

            for pixel in pixels[:-1]:
                if pixel == [x, y]:
                    if game_over_dialog():
                        x = width / 2
                        y = height / 2
                        speed_x = 0
                        speed_y = 0
                        snake_size = 1
                        pixels = []
                        food_x, food_y = generate_food(pixels)
                    else:
                        pygame.quit()
                        sys.exit()

            draw_snake(square_size, pixels)

            draw_score(snake_size - 1)

            if x == food_x and y == food_y:
                snake_size += 1
                food_x, food_y = generate_food(pixels)
        else:
            draw_pause_message()

        pygame.display.update()
        clock.tick(game_speed)

exec_game()