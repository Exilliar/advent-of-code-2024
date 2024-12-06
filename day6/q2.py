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
        self.lines = lines
        self.rows = [list(line.replace("\n", "")) for line in lines]
        self.numCols = len(list(lines[0]))
        self.numRows = len(self.rows)

        self.startY = -1
        self.startX = -1

        self.moveDir = 0 # 0 = up, 1 = right, 2 = down, 3 = left

        for y in range(len(self.rows)):
            row = self.rows[y]
            for x in range(len(row)):
                item = row[x]
                if item == "^":
                    # print("start moving up")
                    self.startY = y
                    self.startX = x
                    self.moveDir = 0
                elif item == ">":
                    # print("start moving right")
                    self.startY = y
                    self.startX = x
                    self.moveDir = 1
                elif item == "v":
                    # print("start moving down")
                    self.startY = y
                    self.startX = x
                    self.moveDir = 2
                elif item == "<":
                    # print("start moving left")
                    self.startY = y
                    self.startX = x
                    self.moveDir = 3
        self.rows[self.startY][self.startX] = "*"

        self.startingMoveDir = self.moveDir
        self.moveFuncs = [up, right, down, left]

        self.coords = [(self.startX, self.startY, 0, self.moveDir)] # x, y, order, moveDir

    def turnFunc(self):
        """Get the function that should be used if the guard turned right now. Does not change any properties"""
        tmpMoveDir = self.moveDir
        if tmpMoveDir + 1 > 3:
            return self.moveFuncs[0]
        return self.moveFuncs[tmpMoveDir + 1]

    def turn90(self):
        self.moveDir += 1
        if self.moveDir > 3:
            self.moveDir = 0
    # check if the current coordinates cross some existing coordinates
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
            # print("loop", str(currX), str(currY))
            i += 1
            # if i > 50:
            #     print("i:", str(i))
            x, y, _ = self.moveFuncs[self.moveDir](currX, currY)
            try:
                val = self.getVal(x, y)
                while val == "#":
                    self.turn90()
                    x, y, _ = self.moveFuncs[self.moveDir](currX, currY)
                    val = self.getVal(x, y)
            except IndexError as error:
                # print("isLoop", error)
                break
            currX = x
            currY = y

            if i != 1:
                # if currently crossing either old coords or new coords or starting coords and are moving in the same direction
                oldCheck = self.checkCross(currX, currY, oldCoords)
                newCheck = self.checkCross(currX, currY, self.coords)
                # startCheck = self.checkCross(currX, currY, [(self.startX, self.startY, 0, self.startingMoveDir)])
                if oldCheck[0] and oldCheck[2] == self.moveDir:
                    # print("old check")
                    # print(currX, currY)
                    return True
                elif newCheck[0] and newCheck[2] == self.moveDir:
                    # print("new check")
                    return True
            # elif startCheck[0] and startCheck[2] == self.moveDir:
            #     return True

            self.coords.append((currX, currY, i, self.moveDir))
        return False

    def moveAround(self):
        currX = self.startX
        currY = self.startY
        i = 0
        count = 0

        while True:
            # print("loop")
            print(i)
            i += 1
            x, y, _ = self.moveFuncs[self.moveDir](currX, currY)
            try:
                val = self.getVal(x, y)
                while val == "#":
                    self.turn90()
                    x, y, _ = self.moveFuncs[self.moveDir](currX, currY)
                    val = self.getVal(x, y)
            except IndexError as error:
                # print(error)
                break
            currX = x
            currY = y

            if self.rows[y][x] != "O":
                self.rows[y][x] = "X"

            # find coords for next blocker
            blockX, blockY, _ = self.moveFuncs[self.moveDir](currX, currY)
            # if self.rows[blockY][blockX] != "#": # no point checking if there's already a blocker where we were testing
            try:
                if self.getVal(blockX, blockY) != "#":
                    lines = []
                    for y in range(len(self.rows)):
                        line = [i for i in self.rows[y]] #"".join(self.rows[y])
                        if y == currY:
                            if self.moveDir == 0:
                                # print("moving up")
                                line[currX] = ">"
                            elif self.moveDir == 1:
                                # print("moving right")
                                line[currX] = "v"
                            elif self.moveDir == 2:
                                # print("moving down")
                                line[currX] = "<"
                            elif self.moveDir == 3:
                                # print("moving left")
                                line[currX] = "^"
                        if y == blockY:
                            line[blockX] = "#"
                        lines.append("".join(line))

                    grid = Grid(lines)
                    if grid.isLoop(self.coords):
                        # print("'successful' loop")
                        # print(grid)
                        count += 1
                        self.rows[blockY][blockX] = "O"
            except IndexError as error:
                # print(error)
                break


            self.coords.append((currX, currY, i, self.moveDir))

        self.rows[self.startY][self.startX] = "*"
        # return len(self.coords)
        return count

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
    # print(grid)
    print("count", str(count))
    with open("out.txt", "w") as fp:
        fp.write(str(grid))
