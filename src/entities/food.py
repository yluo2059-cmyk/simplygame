from dataclasses import dataclass
from typing import Tuple

GridPos = Tuple[int, int]


@dataclass
class Food:
    position: GridPos
