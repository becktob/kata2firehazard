class Grid:
    def __init__(self):
        # indices are [row][col]
        rows = 1000
        cols = 1000
        self._lights = [[False for _ in range(cols)] for _ in range(rows)]

    def count_lit(self):
        return sum((sum(row) for row in self._lights))
