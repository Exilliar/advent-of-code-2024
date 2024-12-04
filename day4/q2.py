def upLeft(x: int, y: int):
    return (x-1, y-1, "upLeft")
def upRight(x: int, y: int):
    return (x+1, y-1, "upRight")
def downRight(x: int, y: int):
    return (x+1, y+1, "downRight")
def downLeft(x: int, y: int):
    return (x-1, y+1, "downLeft")

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
    def invertXY(self, x: int, y: int):
        return not self.checkXY(x, y)
    def checkCross(self, topVal, botVal):
        if not (topVal == "M" or topVal == "S"):
            return False
        if not (botVal == "M" or botVal == "S"):
            return False
        if topVal == "M" and botVal == "S":
            return True
        elif topVal == "S" and botVal == "M":
            return True
        return False

    def findXmas(self, startX: int, startY: int) -> bool:
        currX = startX
        currY = startY
        
        toplx, toply, _ = upLeft(currX, currY)
        botlx, botly, _ = downLeft(currX, currY)
        toprx, topry, _ = upRight(currX, currY)
        botrx, botry, _ = downRight(currX, currY)

        if (self.invertXY(toplx, toply) or self.invertXY(botlx, botly) or self.invertXY(toprx, topry) or self.invertXY(botrx, botry)):
            return False
        
        toplVal = self.rows[toply][toplx]
        botlVal = self.rows[botly][botlx]
        toprVal = self.rows[topry][toprx]
        botrVal = self.rows[botry][botrx]

        return self.checkCross(toplVal, botrVal) and self.checkCross(toprVal, botlVal)

    def __str__(self):
        toReturn = ""
        for row in self.rows:
            toReturn += ", ".join(row) + "\n"
        return toReturn

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.replace("\n", "") for line in lines]
    grid = Grid(lines)
    count = 0
    for y in range(len(lines)):
        for x in range(len(list(lines[y]))):
            if lines[y][x] == "A":
                if (grid.findXmas(x, y)):
                    count += 1
    print(count)
