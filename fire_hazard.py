from typing import Callable


class Grid:
    def __init__(self):
        # indices are [row][col]
        rows = 1000
        cols = 1000
        self._lights = [[False for _ in range(cols)] for _ in range(rows)]

    def count_lit(self):
        return sum((sum(row) for row in self._lights))

    def _apply_operation_to_range(self, row_range_inclusive: tuple[int, int],
                                  col_range_inclusive: tuple[int, int],
                                  operation: Callable[[bool], bool]):
        row_range_inclusive = sorted(row_range_inclusive)
        col_range_inclusive = sorted(col_range_inclusive)
        for col in range(col_range_inclusive[0], col_range_inclusive[1] + 1):
            for row in range(row_range_inclusive[0], row_range_inclusive[1] + 1):
                self._lights[row][col] = operation(self._lights[row][col])

    def turn_on(self, row_range_inclusive: tuple[int, int], col_range_inclusive: tuple[int, int]):
        op = lambda _: True
        self._apply_operation_to_range(row_range_inclusive, col_range_inclusive, op)

    def turn_off(self, row_range_inclusive: tuple[int, int], col_range_inclusive: tuple[int, int]):
        op = lambda _: False
        self._apply_operation_to_range(row_range_inclusive, col_range_inclusive, op)

    def toggle(self, row_range_inclusive: tuple[int, int], col_range_inclusive: tuple[int, int]):
        op = lambda val: not val
        self._apply_operation_to_range(row_range_inclusive, col_range_inclusive, op)
