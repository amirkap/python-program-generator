import pygame
import random

# Initialize pygame
pygame.init()

# Set window size
window_width = 800
window_height = 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake class
class Snake:
    def __init__(self):
        self.size = 1
        self.segments = [(window_width / 2, window_height / 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def move(self):
        x, y = self.segments[0]
        if self.direction == "UP":
            self.segments.insert(0, (x, y - 20))
        elif self.direction == "DOWN":
            self.segments.insert(0, (x, y + 20))
        elif self.direction == "LEFT":
            self.segments.insert(0, (x - 20, y))
        elif self.direction == "RIGHT":
            self.segments.insert(0, (x + 20, y))
        self.segments = self.segments[:self.size]

    def change_direction(self, direction):
        opposite_directions = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if direction != opposite_directions[self.direction]:
            self.direction = direction

    def eat(self):
        self.size += 1

    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(window, GREEN, (segment[0], segment[1], 20, 20))


# Food class
class Food:
    def __init__(self):
        self.position = self._random_position()

    def _random_position(self):
        x = random.randint(0, (window_width - 20) // 20) * 20
        y = random.randint(0, (window_height - 20) // 20) * 20
        return x, y

    def draw(self):
        pygame.draw.rect(window, RED, (self.position[0], self.position[1], 20, 20))


# Game loop
def game_loop():
    snake = Snake()
    food = Food()
    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")

        window.fill(BLACK)

        snake.move()

        if snake.segments[0] == food.position:
            snake.eat()
            food.position = food._random_position()

        if snake.segments[0][0] < 0 or snake.segments[0][0] >= window_width or snake.segments[0][1] < 0 or snake.segments[0][1] >= window_height:
            game_over = True

        for segment in snake.segments[1:]:
            if segment == snake.segments[0]:
                game_over = True

        snake.draw()
        food.draw()

        pygame.display.update()
        clock.tick(10)

    pygame.quit()

# Start the game loop
game_loop()