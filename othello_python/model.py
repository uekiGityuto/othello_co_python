# Othello Model

import numpy as np


class Stone:
    def __init__(self, color: str):
        self.color = color


class Cell:
    def __init__(self, stone: Stone | None = None):
        self.stone = stone

    def put(self, stone):
        self.stone = stone

    def is_empty(self):
        return self.stone is None

    def is_black(self):
        # if black, return True, but stone is None, return False
        return self.stone and self.stone.color == "black"

    def is_white(self):
        # if white, return True, but stone is None, return False
        return self.stone and self.stone.color == "white"

    def flip(self):
        if self.is_black():
            self.stone.color = "white"
        elif self.is_white():
            self.stone.color = "black"
        else:
            raise Exception("Invalid stone color")

    def __str__(self):
        if self.is_empty():
            return " "
        elif self.is_black():
            return "●"
        elif self.is_white():
            return "○"
        else:
            raise Exception("Invalid stone color")


class Board:
    def __init__(self):
        self.cells = np.array([[Cell() for _ in range(8)] for _ in range(8)])
        self.cells = self.cells.T
        self.cells[3][3].put(Stone("white"))
        self.cells[4][4].put(Stone("white"))
        self.cells[3][4].put(Stone("black"))
        self.cells[4][3].put(Stone("black"))

    def can_put_anywhere(self, stone: Stone):
        for x in range(8):
            for y in range(8):
                if self.can_put(x, y, stone):
                    return True
        return False

    def is_full(self):
        for x in range(8):
            for y in range(8):
                if self.cells[x][y].is_empty():
                    return False
        return True

    def can_put(self, x: int, y: int, stone: Stone):
        if not self.cells[x][y].is_empty():
            return False

        for dx, dy in [
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
        ]:
            if self._can_put(x, y, dx, dy, stone):
                return True

        return False

    def _can_put(self, x: int, y: int, dx: int, dy: int, stone: Stone):
        x += dx
        y += dy

        if not (0 <= x < 8 and 0 <= y < 8):
            return False

        if self.cells[x][y].is_empty():
            return False

        if self.cells[x][y].stone.color == stone.color:
            return False

        while True:
            x += dx
            y += dy

            if not (0 <= x < 8 and 0 <= y < 8):
                return False

            if self.cells[x][y].is_empty():
                return False

            if self.cells[x][y].stone.color == stone.color:
                return True

    def put(self, x: int, y: int, stone: Stone):
        if not self.can_put(x, y, stone):
            return False

        self.cells[x][y].put(stone)

        for dx, dy in [
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
        ]:
            self._put(x, y, dx, dy, stone)

        return True

    def _put(self, x: int, y: int, dx: int, dy: int, stone: Stone) -> None:
        x += dx
        y += dy

        if not (0 <= y < 8 and 0 <= x < 8):
            return

        if self.cells[x][y].is_empty():
            return

        if self.cells[x][y].stone.color == stone.color:
            return

        while True:
            x += dx
            y += dy

            if not (0 <= x < 8 and 0 <= y < 8):
                return

            if self.cells[x][y].is_empty():
                return

            if self.cells[x][y].stone.color == stone.color:
                break

        while True:
            x -= dx
            y -= dy

            if self.cells[x][y].stone.color == stone.color:
                return

            self.cells[x][y].flip()

    def count(self, stone):
        return sum(
            [cell.stone.color == stone.color for row in self.cells for cell in row]
        )

    def __str__(self):
        return "\n".join([" ".join([str(cell) for cell in row]) for row in self.cells])
