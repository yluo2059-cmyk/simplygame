from typing import Tuple

from src.entities.snake import Snake

GridPos = Tuple[int, int]


def hits_wall(head: GridPos, grid_width: int, grid_height: int) -> bool:
    return head[0] < 0 or head[1] < 0 or head[0] >= grid_width or head[1] >= grid_height


def hits_self(snake: Snake) -> bool:
    body = list(snake.body)
    return snake.head in body[1:]
