from typing import Tuple

def up(x: int, y: int):
    return (x, y-1, "up")
def right(x: int, y: int):
    return (x+1, y, "right")
def down(x: int, y: int):
    return (x, y+1, "down")
def left(x: int, y: int):
    return (x-1, y, "left")

def makeKey(x: int, y: int, dir: str = ""):
    if dir != "":
        return f"{x},{y},{dir}"
    return f"{x},{y}"

def get(x: int, y: int, grid: list):
    if x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
        return grid[y][x]
    return ""

def checkAndRun(x, y, key, visitedCells, dir: str, grid, perimeterValues: list):
    perimeter = 0
    area = 0
    if get(x, y, grid) == key:
        if makeKey(x, y) in visitedCells:
            return (0, 0)
        area += 1
        (a, p) = findAreaPerim(x, y, grid, visitedCells, key, area, perimeterValues)
        area = a
        perimeter += p
    else:
        perimeter += 1
        perimeterValues.append((x, y, dir))
    return (area, perimeter)

def findAreaPerim(x: int, y: int, grid: list, visitedCells: dict, key: str, area: int, perimeterValues: list) -> Tuple[int, int]: # (area, perim)
    visitedCells[makeKey(x, y)] = (0, 0)
    upPos = up(x, y)
    rightPos = right(x, y)
    downPos = down(x, y)
    leftPos = left(x, y)
    perimeter = 0
    (a, p) = checkAndRun(upPos[0], upPos[1], key, visitedCells, "up", grid, perimeterValues)
    area += a
    perimeter += p

    (a, p) = checkAndRun(downPos[0], downPos[1], key, visitedCells, "down", grid, perimeterValues)
    area += a
    perimeter += p

    (a, p) = checkAndRun(leftPos[0], leftPos[1], key, visitedCells, "left", grid, perimeterValues)
    area += a
    perimeter += p

    (a, p) = checkAndRun(rightPos[0], rightPos[1], key, visitedCells, "right", grid, perimeterValues)
    area += a
    perimeter += p

    visitedCells[makeKey(x, y)] = (area, perimeter)

    return (area, perimeter)

def checkArr(x: int, y: int, dir: str, perimeterValues: list):
    for val in perimeterValues:
        if val[0] == x and val[1] == y and val[2] == dir:
            return True
    return False

def removePerimVals(x: int, y: int, dir: str, perimeterValues: list, perimeterValuesDict, func):
    currX, currY, _ = func(x, y)
    while checkArr(currX, currY, dir, perimeterValues):
        key = makeKey(currX, currY, dir)
        if key in perimeterValuesDict:
            perimeterValuesDict[key] += 1
        else:
            perimeterValuesDict[key] = 1
        currX, currY, _ = func(currX, currY)

def maxReached(x: int, y: int, perimeterValuesDict: dict, perimeterValues: list):
    count = 0
    for val in perimeterValues:
        if val[0] == x and val[1] == y:
            count += 1
    key = makeKey(x, y)
    if perimeterValuesDict[key] == count:
        return False
    return True

with open("input.txt", "r") as f:
    grid = [list(line.replace("\n", "")) for line in f.readlines()]
    visitedCells = {}
    total = 0
    for y in range(len(grid)):
        row = grid[y]
        for x in range(len(row)):
            cell = row[x]
            if makeKey(x, y) not in visitedCells:
                perimeterValues = []
                (area, perimeter) = findAreaPerim(x, y, grid, visitedCells, cell, 0, perimeterValues)
                area += 1
                perimeterValuesDict = {}
                sides = 0
                for val in perimeterValues:
                    xx = val[0]
                    yy = val[1]
                    dir = val[2]
                    if makeKey(xx, yy, dir) not in perimeterValuesDict:
                        sides += 1
                        perimeterValuesDict[makeKey(xx, y)] = True
                        if dir == "up" or dir == "down":
                            removePerimVals(xx, yy, dir, perimeterValues, perimeterValuesDict, left)
                            removePerimVals(xx, yy, dir, perimeterValues, perimeterValuesDict, right)
                        else:
                            removePerimVals(xx, yy, dir, perimeterValues, perimeterValuesDict, up)
                            removePerimVals(xx, yy, dir, perimeterValues, perimeterValuesDict, down)

                cost = area * sides
                total += cost
    print(total)
