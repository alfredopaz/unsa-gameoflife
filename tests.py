import pytest
from model.model import step

@pytest.mark.parametrize('grid, expected', [
  (['.....', '..O..', '.....'], ['.....', '.....', '.....']),
  (['.....', '.OO..', '.OO..'], ['.....', '.OO..', '.OO..']),
])
def test_step(grid, expected):
  assert step(grid) == expected
