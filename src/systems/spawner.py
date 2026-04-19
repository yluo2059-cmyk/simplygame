import random
from typing import Iterable, Tuple

GridPos = Tuple[int, int]


def spawn_food(grid_width: int, grid_height: int, blocked: Iterable[GridPos]) -> GridPos:
    blocked_set = set(blocked)
    available = [
        (x, y)
        for x in range(grid_width)
        for y in range(grid_height)
        if (x, y) not in blocked_set
    ]
    if not available:
        return (0, 0)
    return random.choice(available)
