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

    def test_light_turns_off(self):
        grid = Grid()

        grid.turn_on((1, 10), (1, 10))
        self.assertEqual(100, grid.count_lit())

        grid.turn_off((9, 999), (5, 6))
        # 9-10 x 5-6 = 4 turned off
        self.assertEqual(96, grid.count_lit())

    def test_toggle(self):
        grid = Grid()

        grid.turn_on((1, 10), (1, 10))
        self.assertEqual(100, grid.count_lit())

        grid.toggle((5, 5), (5, 12))
        self.assertEqual(96, grid.count_lit())
