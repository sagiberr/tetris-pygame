import pygame
from constants import SHAPES, COLORS, COLS, CELL_SIZE, BLACK, ROWS

class Tetromino:
    def __init__(self, shape_id):
        self.shape_id = shape_id
        self.shape = SHAPES[shape_id]
        self.color = COLORS[shape_id]
        self.x = COLS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def draw(self, surface):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    rect = pygame.Rect((self.x + j) * CELL_SIZE, (self.y + i) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(surface, self.color, rect)
                    pygame.draw.rect(surface, BLACK, rect, 1)
    
    def move(self, dx, dy):
        self.x += dx 
        self.y += dy

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]


class Board:
    def __init__(self):
        self.grid = [[None for _ in range(COLS)] for _ in range(ROWS)]

    def is_valid_position(self, tetromino, dx=0, dy=0):
        for i, row in enumerate(tetromino.shape):
            for j, cell in enumerate(row):
                if cell:
                    new_x = tetromino.x + j + dx
                    new_y = tetromino.y + i + dy
                    if new_x < 0 or new_x >= COLS or new_y >= ROWS:
                        return False
                    if new_y >= 0 and self.grid[new_y][new_x]:
                        return False
        return True

    def lock_tetromino(self, tetromino):
        for i, row in enumerate(tetromino.shape):
            for j, cell in enumerate(row):
                if cell:
                    x = tetromino.x + j
                    y = tetromino.y + i
                    if y >= 0:
                        self.grid[y][x] = tetromino.color

    def draw(self, surface):
        for y in range(ROWS):
            for x in range(COLS):
                cell = self.grid[y][x]
                if cell:
                    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(surface, cell, rect)
                    pygame.draw.rect(surface, BLACK, rect, 1)

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell is None for cell in row)]
        lines_cleared = ROWS - len(new_grid)
        while len(new_grid) < ROWS:
            new_grid.insert(0, [None for _ in range(COLS)])
        self.grid = new_grid
        return lines_cleared
