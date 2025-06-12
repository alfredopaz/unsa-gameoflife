import argparse
import sys
from model.board import Board
from controller.controller import Controller

def parse_args():
  parser = argparse.ArgumentParser(description="Juego de la Vida MVC")
  parser.add_argument(
    '-f', '--pattern-file',
    help="Archivo de texto con patrón inicial (una fila por línea, 'O' viva, '.' muerta)"
  )
  parser.add_argument(
    '--fps', type=int, default=5,
    help="Frames por segundo"
  )
  return parser.parse_args()

def main():
  args = parse_args()
  if args.pattern_file:
    try:
      with open(args.pattern_file, 'r') as f:
        lines = [line.rstrip('\n') for line in f if line.strip()]
      board = Board(lines)
    except Exception as e:
      print(f"Error al leer patrón desde '{args.pattern_file}': {e}", file=sys.stderr)
      sys.exit(1)
  else:
    board = Board.blinker(width=10, height=3)

  controller = Controller(board, fps=args.fps)
  controller.run()

if __name__ == '__main__':
  main()
