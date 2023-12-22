import sys
import pygame
from configs.configs import green, screen, width, height, white

# Score game
def draw_score(score):
    font = pygame.font.SysFont("Helvetica", 15)
    text = font.render(f"Score: {score}", True, green)
    screen.blit(text, [1, 1])

#  pause game
def draw_pause_message():
    font = pygame.font.SysFont("Helvetica", 15)
    text = font.render("Paused - Press any key to continue", True, white)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)

# Game over
def game_over_dialog():
    font = pygame.font.SysFont("Helvetica", 15)
    text = font.render("Game Over! Play again? (Y/N)", True, white)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()