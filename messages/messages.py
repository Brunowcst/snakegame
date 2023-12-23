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
def game_over_dialog(score):
    font = pygame.font.SysFont("Helvetica", 15)
    game_over_text = font.render("Game Over!", True, white)
    score_text = font.render(f"Score: {score}", True, white)
    play_again_text = font.render("Play again? (Y/N)", True, white)

    game_over_rect = game_over_text.get_rect(center=(width // 2, height // 2 - 20))
    score_rect = score_text.get_rect(center=(width // 2, height // 2))
    play_again_rect = play_again_text.get_rect(center=(width // 2, height // 2 + 20))

    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    screen.blit(play_again_text, play_again_rect)
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