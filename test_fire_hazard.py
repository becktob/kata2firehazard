from unittest import TestCase

from fire_hazard import Grid


class TestGrid(TestCase):
    def test_initialized_grid_is_off(self):
        grid = Grid()
        self.assertEquals(0, grid.count_lit())
