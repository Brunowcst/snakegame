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

    if len(pixels) > 0:
        head_x, head_y = pixels[-1]
        eye_size = size // 3
        eye_offset = size // 10

        eye1_x = head_x + eye_offset
        eye1_y = head_y + eye_offset
        eye2_x = head_x + size - eye_offset - eye_size
        eye2_y = head_y + eye_offset

        pygame.draw.rect(screen, red, [eye1_x, eye1_y, eye_size, eye_size])
        pygame.draw.rect(screen, red, [eye2_x, eye2_y, eye_size, eye_size])

def draw_score(score):
    font = pygame.font.SysFont("Helvetica", 15)
    text = font.render(f"Score: {score}", True, green)
    screen.blit(text, [1, 1])

def draw_pause_message():
    font = pygame.font.SysFont("Helvetica", 15)
    text = font.render("Paused - Press any key to continue", True, white)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)

def select_speed(key, current_speed):
    speed_x, speed_y = current_speed

    if key == pygame.K_DOWN and speed_y != -square_size:
        speed_x = 0
        speed_y = square_size
    elif key == pygame.K_UP and speed_y != square_size:
        speed_x = 0
        speed_y = -square_size
    elif key == pygame.K_RIGHT and speed_x != -square_size:
        speed_x = square_size
        speed_y = 0
    elif key == pygame.K_LEFT and speed_x != square_size:
        speed_x = -square_size
        speed_y = 0
    elif key == pygame.K_s and speed_y != -square_size:
        speed_x = 0
        speed_y = square_size
    elif key == pygame.K_w and speed_y != square_size:
        speed_x = 0
        speed_y = -square_size
    elif key == pygame.K_d and speed_x != -square_size:
        speed_x = square_size
        speed_y = 0
    elif key == pygame.K_a and speed_x != square_size:
        speed_x = -square_size
        speed_y = 0
    elif key == pygame.K_p or key == pygame.K_SPACE:
        speed_x = 0
        speed_y = 0
    else:
        return current_speed
    return speed_x, speed_y

def exec_game():
    end_game = False
    game_paused = False

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
                end_game = True

            x += speed_x
            y += speed_y

            # draw snake
            pixels.append([x, y])

            if len(pixels) > snake_size:
                del pixels[0]

            for pixel in pixels[:-1]:
                if pixel == [x, y]:
                    end_game = True

            draw_snake(square_size, pixels)

            draw_score(snake_size - 1)

            if x == food_x and y == food_y:
                snake_size += 1
                food_y, food_y = generate_food()
        else:
            draw_pause_message()

        pygame.display.update()
        clock.tick(game_speed)

exec_game()