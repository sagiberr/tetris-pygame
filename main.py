import pygame
import sys
import random
from constants import SHAPES, COLORS, CELL_SIZE, COLS, ROWS, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, GRAY, FPS
from tetris import Tetromino, Board

pygame.init()
font = pygame.font.SysFont("Arial", 24)

# screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# refresh rate
clock = pygame.time.Clock()
fall_time = 0
fall_speed = 0.1  # seconds between falls
score = 0

# draw grid
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

# create initial block and board
current_piece = Tetromino(random.choice(list(SHAPES.keys())))
board = Board()

# game loop
running = True
while running:
    screen.fill(BLACK)
    draw_grid()
    board.draw(screen)
    current_piece.draw(screen)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    fall_time += clock.get_rawtime() / 1000
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if board.is_valid_position(current_piece, dx=-1):
                    current_piece.move(-1, 0)

            elif event.key == pygame.K_RIGHT:
                if board.is_valid_position(current_piece, dx=1):
                    current_piece.move(1, 0)

            elif event.key == pygame.K_DOWN:
                if board.is_valid_position(current_piece, dy=1):
                    current_piece.move(0, 1)

            elif event.key == pygame.K_r:
                current_piece.rotate()
                if not board.is_valid_position(current_piece):
                    for _ in range(3):
                        current_piece.rotate()

    # auto fall
    if fall_time >= fall_speed:
        if board.is_valid_position(current_piece, dy=1):
            current_piece.move(0, 1)
        else:
            board.lock_tetromino(current_piece)
            lines_cleared = board.clear_lines()
            score += lines_cleared * 100
            current_piece = Tetromino(random.choice(list(SHAPES.keys())))
            if not board.is_valid_position(current_piece):
                print("Game Over!")
                running = False
        fall_time = 0

    pygame.display.update()

pygame.quit()
sys.exit()
