import pygame

from src.entities.snake import Snake
from src.state import GameState

DIRECTION_MAP = {
    pygame.K_UP: (0, -1),
    pygame.K_w: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_s: (0, 1),
    pygame.K_LEFT: (-1, 0),
    pygame.K_a: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_d: (1, 0),
}


def apply_key(key: int, snake: Snake, state: GameState) -> GameState:
    if key in DIRECTION_MAP and state == GameState.RUNNING:
        snake.set_direction(DIRECTION_MAP[key])
        return state

    if key == pygame.K_p and state in (GameState.RUNNING, GameState.PAUSED):
        return GameState.PAUSED if state == GameState.RUNNING else GameState.RUNNING

    return state
