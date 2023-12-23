import sys
import pygame

from configs.configs import *
from snake.snake import draw_snake
from messages.messages import *
from food.food import draw_food, generate_food
from controls.controls import select_speed

pygame.init()
pygame.display.set_caption("Snake game")

def difficulty_selection():
    font = pygame.font.SysFont("Helvetica", 20)
    text_easy = font.render("Easy", True, white)
    text_medium = font.render("Medium", True, white)
    text_hard = font.render("Hard", True, white)

    easy_rect = text_easy.get_rect(center=(width // 2, height // 4))
    medium_rect = text_medium.get_rect(center=(width // 2, height // 2))
    hard_rect = text_hard.get_rect(center=(width // 2, 3 * height // 4))

    while True:
        screen.fill(black)
        screen.blit(text_easy, easy_rect)
        screen.blit(text_medium, medium_rect)
        screen.blit(text_hard, hard_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if easy_rect.collidepoint(x, y):
                    return "easy"
                elif medium_rect.collidepoint(x, y):
                    return "medium"
                elif hard_rect.collidepoint(x, y):
                    return "hard"
                
def get_game_speed(difficulty):
    if difficulty == "easy":
        return 10
    elif difficulty == "medium":
        return 15
    elif difficulty == "hard":
        return 20
    else:
        # Default speed
        return 15

def exec_game(difficult):
    end_game = False
    game_paused = False

    game_speed = get_game_speed(difficult)

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
                if game_over_dialog(snake_size - 1):
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
                    if game_over_dialog(snake_size - 1):
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

            if snake_size == (width // square_size) * (height // square_size):
                end_game = True
                game_win_dialog(snake_size - 1)
        else:
            draw_pause_message()

        pygame.display.update()
        clock.tick(game_speed)

selected_difficulty = difficulty_selection()

exec_game(selected_difficulty)