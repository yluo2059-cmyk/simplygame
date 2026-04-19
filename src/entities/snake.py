from collections import deque
from typing import Deque, Iterable, Tuple

GridPos = Tuple[int, int]


class Snake:
    def __init__(self, start_pos: GridPos) -> None:
        self.body: Deque[GridPos] = deque([start_pos, (start_pos[0] - 1, start_pos[1])])
        self.direction: GridPos = (1, 0)
        self.pending_growth = 0

    @property
    def head(self) -> GridPos:
        return self.body[0]

    def set_direction(self, new_direction: GridPos) -> None:
        # Prevent immediate 180-degree reversal.
        if (new_direction[0] * -1, new_direction[1] * -1) == self.direction:
            return
        self.direction = new_direction

    def move(self) -> None:
        next_head = (self.head[0] + self.direction[0], self.head[1] + self.direction[1])
        self.body.appendleft(next_head)
        if self.pending_growth > 0:
            self.pending_growth -= 1
            return
        self.body.pop()

    def grow(self, amount: int = 1) -> None:
        self.pending_growth += amount

    def contains(self, pos: GridPos) -> bool:
        return pos in self.body

    def positions(self) -> Iterable[GridPos]:
        return tuple(self.body)
