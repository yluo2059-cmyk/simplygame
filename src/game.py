import pygame

from src import config
from src.entities.food import Food
from src.entities.snake import Snake
from src.state import GameState
from src.systems.collision import hits_self, hits_wall
from src.systems.input_handler import apply_key
from src.systems.spawner import spawn_food
from src.ui.hud import draw as draw_hud
from src.ui.renderer import render


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(config.TITLE)

        self.screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 28)

        self.grid_width = config.WINDOW_WIDTH // config.GRID_SIZE
        self.grid_height = config.WINDOW_HEIGHT // config.GRID_SIZE

        self.running = True
        self.state = GameState.RUNNING
        self.score = 0

        self._setup_round()

    def _setup_round(self) -> None:
        start = (self.grid_width // 2, self.grid_height // 2)
        self.snake = Snake(start)
        self.food = Food(spawn_food(self.grid_width, self.grid_height, self.snake.positions()))

    def _restart(self) -> None:
        self.score = 0
        self.state = GameState.RUNNING
        self._setup_round()

    def _tick(self) -> None:
        if self.state != GameState.RUNNING:
            return

        self.snake.move()
        if hits_wall(self.snake.head, self.grid_width, self.grid_height) or hits_self(self.snake):
            self.state = GameState.GAME_OVER
            return

        if self.snake.head == self.food.position:
            self.score += 1
            self.snake.grow()
            self.food = Food(spawn_food(self.grid_width, self.grid_height, self.snake.positions()))

    def run(self) -> None:
        move_accumulator = 0
        while self.running:
            dt = self.clock.tick(config.FPS)
            move_accumulator += dt

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        break
                    if event.key == pygame.K_r and self.state == GameState.GAME_OVER:
                        self._restart()
                        move_accumulator = 0
                        continue
                    self.state = apply_key(event.key, self.snake, self.state)

            while move_accumulator >= config.TICK_MS and self.running:
                self._tick()
                move_accumulator -= config.TICK_MS

            render(self.screen, self.snake, self.food)
            draw_hud(self.screen, self.font, self.score, self.state)
            pygame.display.flip()

        pygame.quit()
