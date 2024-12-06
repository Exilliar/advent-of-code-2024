from typing import Callable

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

class Grid:
    def __init__(self, lines):
        self.rows = [list(line.replace("\n", "")) for line in lines]
        self.numCols = len(list(lines[0]))
        self.numRows = len(self.rows)

        self.startY = -1
        self.startX = -1

        for y in range(len(self.rows)):
            row = self.rows[y]
            for x in range(len(row)):
                item = row[x]
                if item == "^":
                    self.startY = y
                    self.startX = x

        self.moveDir = 0 # 0 = up, 1 = right, 2 = down, 3 = left
        self.moveFuncs = [up, right, down, left]

        self.coords = { f"{self.startX},{self.startY}": True} # "x,y"

    def turn90(self):
        self.moveDir += 1
        if self.moveDir > 3:
            self.moveDir = 0

    def moveAround(self):
        currX = self.startX
        currY = self.startY

        while True:
            x, y, _ = self.moveFuncs[self.moveDir](currX, currY)
            try:
                val = self.getVal(x, y)
                while val == "#":
                    self.turn90()
                    x, y, _ = self.moveFuncs[self.moveDir](currX, currY)
                    val = self.getVal(x, y)
                currX = x
                currY = y
                self.coords[str(currX) + "," + str(currY)] = True

                self.rows[y][x] = "X"
            except IndexError:
                break
        self.rows[self.startY][self.startX] = "*"
        return len(self.coords)

    def checkXY(self, x: int, y: int):
        if (x < 0 or x >= self.numCols):
            return False
        if (y < 0 or y >= self.numRows):
            return False
        return True

    def invertXY(self, x: int, y: int):
        return not self.checkXY(x, y)

    def getVal(self, x, y):
        if (self.checkXY(x, y)):
            return self.rows[y][x]
        else:
            raise IndexError("out of range")

    def __str__(self):
        toReturn = ""
        for row in self.rows:
            toReturn += "".join(row) + "\n"
        return toReturn

with open("input.txt", "r") as f:
    lines = f.readlines()
    grid = Grid(lines)
    count = grid.moveAround()
    print(count)
