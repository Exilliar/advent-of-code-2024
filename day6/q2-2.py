# THIS ONE DOES WORK. IT'S VERY SLOW. I'M VERY ANGRY ABOUT THIS

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

        self.coords = [(self.startX, self.startY, 0, self.moveDir)] # x, y, order, moveDir
        self.disCoords = { f"{self.startX},{self.startY}": True}

    def turn90(self):
        self.moveDir += 1
        if self.moveDir > 3:
            self.moveDir = 0

    def checkCross(self, x, y, coords):
        for coord in coords:
            if coord[0] == x and coord[1] == y:
                return (True, coord[2], coord[3])
        return (False, -1, -1)

    def isLoop(self, oldCoords):
        currX = self.startX
        currY = self.startY
        i = 0
        while True:
            i += 1
            x, y, _ = self.moveFuncs[self.moveDir](currX, currY)
            try:
                val = self.getVal(x, y)
                while val == "#" or val == "O":
                    self.turn90()
                    x, y, _ = self.moveFuncs[self.moveDir](currX, currY)
                    val = self.getVal(x, y)
            except IndexError as error:
                # print("isLoop", error)
                break
            currX = x
            currY = y

            # if currently crossing either old coords or new coords or starting coords and are moving in the same direction
            oldCheck = self.checkCross(currX, currY, oldCoords)
            newCheck = self.checkCross(currX, currY, self.coords)
            startCheck = self.checkCross(currX, currY, [(self.startX, self.startY, 0, 0)])
            if oldCheck[0] and oldCheck[2] == self.moveDir:
                return True
            elif newCheck[0] and newCheck[2] == self.moveDir:
                return True
            elif startCheck[0] and startCheck[2] == self.moveDir:
                return True

            self.coords.append((currX, currY, i, self.moveDir))
        return False

    def moveAround(self):
        currX = self.startX
        currY = self.startY
        i = 0

        while True:
            i += 1
            x, y, _ = self.moveFuncs[self.moveDir](currX, currY)
            try:
                val = self.getVal(x, y)
                while val == "#":
                    self.turn90()
                    x, y, _ = self.moveFuncs[self.moveDir](currX, currY)
                    val = self.getVal(x, y)
                currX = x
                currY = y
                self.disCoords[str(currX) + "," + str(currY)] = True
                self.coords.append((currX, currY, i, self.moveDir))
                # self.coords.append

                self.rows[y][x] = "X"
            except IndexError:
                break
        self.rows[self.startY][self.startX] = "*"
        return self.disCoords

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
    coords = grid.moveAround()
    count = 0
    print("total coords:", len(coords))
    i = 0
    for coord in coords:
        i += 1
        [x, y] = coord.split(",")
        x = int(x)
        y = int(y)
        newLines = []
        for lineY in range(len(lines)):
            line = list(lines[lineY].replace("\n", ""))
            if lineY == y:
                line[x] = "O"
            newLines.append("".join(line))
        testGrid = Grid(newLines)
        if testGrid.isLoop([]):
            print(i, coord, "loop")
            count += 1
        else:
            print(i, coord, "no loop")

    print(count)
