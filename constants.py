SHAPES = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1],
          [1, 1]],
    'T': [[1, 1, 1],
          [0, 1, 0]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'Z': [[1, 1, 0],
          [0, 1, 1]],
    'L': [[1, 0, 0],
          [1, 1, 1]],
    'J': [[0, 0, 1],
          [1, 1, 1]]
}

COLORS = {
    'I': (0, 255, 255),
    'O': (255, 255, 0),
    'T': (160, 0, 240),
    'S': (0, 255, 0),
    'Z': (255, 0, 0),
    'L': (255, 165, 0),
    'J': (0, 0, 255)
}

CELL_SIZE = 30
COLS = 10
ROWS = 20
SCREEN_WIDTH = COLS * CELL_SIZE
SCREEN_HEIGHT = ROWS * CELL_SIZE

BLACK = (0, 0, 0)
GRAY = (40, 40, 40)

FPS = 60
