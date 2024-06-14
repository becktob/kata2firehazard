from unittest import TestCase

from fire_hazard import Grid


class TestGrid(TestCase):
    def test_initialized_grid_is_off(self):
        grid = Grid()
        self.assertEqual(0, grid.count_lit())


    def test_light_turns_on(self):
        grid = Grid()

        grid.turn_on((9, 11), (42, 45))

        self.assertEqual(12, grid.count_lit())
