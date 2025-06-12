import pygame
from model.board import Board
from view.view import View

class Controller:
  def __init__(self, board: Board, fps=10):
    self.board = board
    self.view = View(self.board.grid, cell_size=20)
    self.fps = fps
    self.running = True

  def run(self):
    """Bucle principal: manejo de eventos y actualización."""
    while self.running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.running = False

      self.board.step()
      self.view.grid = self.board.grid
      self.view.draw()
      self.view.clock.tick(self.fps)

    pygame.quit()
