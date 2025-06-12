from typing import List

class Board:
  def __init__(self, grid: List[str]):
    self.grid = grid

  @classmethod
  def blinker(cls, width: int, height: int) -> "Board":
    grid = ["." * width for _ in range(height)]
    mid_y = height // 2
    mid_x = width // 2 - 1
    row = list(grid[mid_y])
    row[mid_x:mid_x+3] = ["O", "O", "O"]
    grid[mid_y] = "".join(row)
    return cls(grid)

  def step(self) -> None:
    from model.model import step as step_fn
    self.grid = step_fn(self.grid)
