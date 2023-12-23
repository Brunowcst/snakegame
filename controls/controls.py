import pygame
from configs.configs import square_size

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