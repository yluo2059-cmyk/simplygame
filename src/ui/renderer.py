import pygame

from src import config
from src.entities.food import Food
from src.entities.snake import Snake


def draw_grid_object(surface: pygame.Surface, pos: tuple[int, int], color: tuple[int, int, int]) -> None:
    rect = pygame.Rect(
        pos[0] * config.GRID_SIZE,
        pos[1] * config.GRID_SIZE,
        config.GRID_SIZE,
        config.GRID_SIZE,
    )
    pygame.draw.rect(surface, color, rect)


def render(surface: pygame.Surface, snake: Snake, food: Food) -> None:
    surface.fill(config.BG_COLOR)

    for pos in snake.positions():
        draw_grid_object(surface, pos, config.SNAKE_COLOR)

    draw_grid_object(surface, food.position, config.FOOD_COLOR)
