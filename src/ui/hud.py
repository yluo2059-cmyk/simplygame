import pygame

from src import config
from src.state import GameState


def draw(surface: pygame.Surface, font: pygame.font.Font, score: int, state: GameState) -> None:
    score_text = font.render(f"Score: {score}", True, config.TEXT_COLOR)
    surface.blit(score_text, (10, 10))

    if state == GameState.PAUSED:
        msg = font.render("Paused (P to resume)", True, config.TEXT_COLOR)
        surface.blit(msg, (10, 40))
    elif state == GameState.GAME_OVER:
        msg = font.render("Game Over (R to restart)", True, config.TEXT_COLOR)
        surface.blit(msg, (10, 40))
