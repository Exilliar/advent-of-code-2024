from typing import Callable

class Grid:
    def __init__(self, lines: list[str]):
        self.rows = [list(line.replace("\n", "")) for line in lines]
        self.numCols = len(list(lines[0]))
        self.numRows = len(self.rows)

    def checkXY(self, x: int, y: int):
        if (x < 0 or x >= self.numCols):
            return False
        if (y < 0 or y >= self.numRows):
            return False
        return True

    def findXmas(self, startX: int, startY: int, inc: Callable[[int, int], tuple[int, int, str]]) -> bool:
        xmas = list("XMAS")
        currX = startX
        currY = startY
        for i, letter in enumerate(xmas):
            if letter != self.rows[currY][currX]:
                return False
            if i != len(xmas) - 1:
                currX, currY, _ = inc(currX, currY)
                if (not self.checkXY(currX, currY)):
                    return False
        return True

    def __str__(self):
        toReturn = ""
        for row in self.rows:
            toReturn += ", ".join(row) + "\n"
        return toReturn

def upLeft(x: int, y: int):
    return (x-1, y-1, "upLeft")
def up(x: int, y: int):
    return (x, y-1, "up")
def upRight(x: int, y: int):
    return (x+1, y-1, "upRight")
def right(x: int, y: int):
    return (x+1, y, "right")
def downRight(x: int, y: int):
    return (x+1, y+1, "downRight")
def down(x: int, y: int):
    return (x, y+1, "down")
def downLeft(x: int, y: int):
    return (x-1, y+1, "downLeft")
def left(x: int, y: int):
    return (x-1, y, "left")

checks = [upLeft, up, upRight, right, downRight, down, downLeft, left]

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.replace("\n", "") for line in lines]
    grid = Grid(lines)
    count = 0
    for y in range(len(lines)):
        for x in range(len(list(lines[y]))):
            if lines[y][x] == "X":
                for check in checks:
                    if (grid.findXmas(x, y, check)):
                        count += 1
    print(count)
