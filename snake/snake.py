import pygame
from configs.configs import screen, white, red

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