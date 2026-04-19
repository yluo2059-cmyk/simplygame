from src.entities.snake import Snake


def test_snake_moves_forward() -> None:
    snake = Snake((5, 5))
    snake.move()
    assert snake.head == (6, 5)
