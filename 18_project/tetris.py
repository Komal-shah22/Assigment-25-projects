import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Global Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
COLUMNS = SCREEN_WIDTH // BLOCK_SIZE
ROWS = SCREEN_HEIGHT // BLOCK_SIZE

WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
COLORS = [(0, 255, 255), (0, 0, 255), (255, 165, 0), 
          (255, 255, 0), (0, 255, 0), (128, 0, 128), (255, 0, 0)]

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1], [1, 1]],  # O
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]]  # L
]

class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = random.choice(COLORS)
        self.x = COLUMNS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def draw(self, screen):
        for i, row in enumerate(self.shape):
            for j, val in enumerate(row):
                if val:
                    pygame.draw.rect(screen, self.color,
                                     (self.x + j) * BLOCK_SIZE, (self.y + i) * BLOCK_SIZE,
                                     BLOCK_SIZE, BLOCK_SIZE)

def check_collision(grid, tetro, dx=0, dy=0, rotate=False):
    shape = tetro.shape
    if rotate:
        shape = [list(row) for row in zip(*shape[::-1])]
    for i, row in enumerate(shape):
        for j, val in enumerate(row):
            if val:
                new_x = tetro.x + j + dx
                new_y = tetro.y + i + dy
                if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS:
                    return True
                if new_y >= 0 and grid[new_y][new_x]:
                    return True
    return False

def lock_piece(grid, tetro):
    for i, row in enumerate(tetro.shape):
        for j, val in enumerate(row):
            if val:
                grid[tetro.y + i][tetro.x + j] = tetro.color

def clear_lines(grid):
    full_rows = [i for i in range(ROWS) if all(grid[i])]
    for i in full_rows:
        del grid[i]
        grid.insert(0, [0] * COLUMNS)

def draw_grid(screen, grid):
    for y in range(ROWS):
        for x in range(COLUMNS):
            color = grid[y][x] if grid[y][x] else GRAY
            pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
            pygame.draw.rect(screen, BLACK, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def welcome():
    print("\n\t~~~~~~~~~~ WELCOME TO TETRIS! ~~~~~~~~~~")
    print("Use arrow keys to move and rotate blocks.")
    print("Clear rows by filling them up.\n")

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    grid = [[0] * COLUMNS for _ in range(ROWS)]
    current_piece = Tetromino()
    fall_time = 0
    fall_speed = 0.3
    running = True

    while running:
        screen.fill(WHITE)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= fall_speed:
            if not check_collision(grid, current_piece, dy=1):
                current_piece.y += 1
            else:
                lock_piece(grid, current_piece)
                clear_lines(grid)
                current_piece = Tetromino()
                if check_collision(grid, current_piece):
                    print("Game Over!")
                    running = False
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(grid, current_piece, dx=-1):
                    current_piece.x -= 1
                elif event.key == pygame.K_RIGHT and not check_collision(grid, current_piece, dx=1):
                    current_piece.x += 1
                elif event.key == pygame.K_DOWN and not check_collision(grid, current_piece, dy=1):
                    current_piece.y += 1
                elif event.key == pygame.K_UP and not check_collision(grid, current_piece, rotate=True):
                    current_piece.rotate()

        draw_grid(screen, grid)
        for i, row in enumerate(current_piece.shape):
            for j, val in enumerate(row):
                if val:
                    pygame.draw.rect(screen, current_piece.color,
                                     ((current_piece.x + j) * BLOCK_SIZE, (current_piece.y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.update()

while True:
    welcome()
    main()
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thanks for playing Tetris!\n")
        break
