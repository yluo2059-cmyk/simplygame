from src.entities.snake import Snake
from src.systems.collision import hits_wall


def test_hits_wall_left() -> None:
    assert hits_wall((-1, 0), 10, 10)


def test_hits_wall_inside() -> None:
    assert not hits_wall((5, 5), 10, 10)


def test_no_self_collision_initially() -> None:
    snake = Snake((3, 3))
    assert snake.head not in list(snake.body)[1:]
