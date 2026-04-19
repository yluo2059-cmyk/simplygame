from enum import Enum, auto


class GameState(Enum):
    RUNNING = auto()
    PAUSED = auto()
    GAME_OVER = auto()
