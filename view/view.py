import pygame

class View:
  def __init__(self, grid, cell_size=20):
    pygame.init()
    self.grid = grid
    self.cell_size = cell_size
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    width = cols * cell_size
    height = rows * cell_size
    self.screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Conway's Game of Life")
    self.clock = pygame.time.Clock()

  def draw(self):
    """Dibuja la grilla en pantalla."""
    self.screen.fill((0, 0, 0))
    for y, row in enumerate(self.grid):
      for x, cell in enumerate(row):
        if cell == 'O':
          rect = pygame.Rect(
            x * self.cell_size,
            y * self.cell_size,
            self.cell_size,
            self.cell_size
          )
          pygame.draw.rect(self.screen, (255, 255, 255), rect)
    pygame.display.flip()
