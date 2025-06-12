from typing import List

def step(grid: List[str]) -> List[str]:
  """Aplica una generación del Juego de la Vida.
  'O' = viva, '.' = muerta."""
  rows = len(grid)
  cols = len(grid[0]) if rows > 0 else 0
  new_grid: List[str] = []

  for y in range(rows):
    new_row = []
    for x in range(cols):
      live_neighbors = 0
      for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
          if dy == 0 and dx == 0:
            continue
          ny, nx = y + dy, x + dx
          if 0 <= ny < rows and 0 <= nx < cols and grid[ny][nx] == 'O':
            live_neighbors += 1

      if grid[y][x] == 'O':
        new_row.append('O' if live_neighbors in (2, 3) else '.')
      else:
        new_row.append('O' if live_neighbors == 3 else '.')

    new_grid.append(''.join(new_row))

  return new_grid
