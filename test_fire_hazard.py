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

    def test_light_turns_on_reverse_indices(self):
        grid = Grid()

        grid.turn_on((11, 9), (42, 45))
        self.assertEqual(12, grid.count_lit())

        grid_2 = Grid()

        grid_2.turn_on((11, 9), (45, 42))
        self.assertEqual(12, grid_2.count_lit())

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

    def test_instructions(self):
        grid = Grid()
        grid.turn_on((887, 9), (959, 629))
        grid.turn_on((454, 398), (844, 448))
        grid.turn_off((539, 243), (559, 965))
        grid.turn_off((370, 819), (676, 868))
        grid.turn_off((145, 40), (370, 997))
        grid.turn_off((301, 3), (808, 453))
        grid.turn_on((351, 678), (951, 908))
        grid.toggle((720, 196), (897, 994))
        grid.toggle((831, 394), (904, 860))

        self.assertEqual(100239, grid.count_lit())
