from typing import Tuple

def up(x: int, y: int):
    return (x, y-1, "up")
def right(x: int, y: int):
    return (x+1, y, "right")
def down(x: int, y: int):
    return (x, y+1, "down")
def left(x: int, y: int):
    return (x-1, y, "left")

def makeKey(x: int, y: int):
    return f"{x},{y}"

def get(x: int, y: int, grid: list):
    if x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
        return grid[y][x]
    return ""

def checkAndRun(x, y, key, visitedCells, dir: str, grid):
    perimeter = 0
    area = 0
    if get(x, y, grid) == key:
        if makeKey(x, y) in visitedCells:
            return (0, 0)
        area += 1
        (a, p) = findAreaPerim(x, y, grid, visitedCells, key, area)
        area = a
        perimeter += p
    else:
        perimeter += 1
    return (area, perimeter)

def findAreaPerim(x: int, y: int, grid: list, visitedCells: dict, key: str, area: int) -> Tuple[int, int]: # (area, perim)
    visitedCells[makeKey(x, y)] = (0, 0)
    upPos = up(x, y)
    rightPos = right(x, y)
    downPos = down(x, y)
    leftPos = left(x, y)
    perimeter = 0
    (a, p) = checkAndRun(upPos[0], upPos[1], key, visitedCells, "up", grid)
    area += a
    perimeter += p

    (a, p) = checkAndRun(downPos[0], downPos[1], key, visitedCells, "down", grid)
    area += a
    perimeter += p

    (a, p) = checkAndRun(leftPos[0], leftPos[1], key, visitedCells, "left", grid)
    area += a
    perimeter += p

    (a, p) = checkAndRun(rightPos[0], rightPos[1], key, visitedCells, "right", grid)
    area += a
    perimeter += p

    visitedCells[makeKey(x, y)] = (area, perimeter)

    return (area, perimeter)

with open("input.txt", "r") as f:
    grid = [list(line.replace("\n", "")) for line in f.readlines()]
    visitedCells = {}
    total = 0
    for y in range(len(grid)):
        row = grid[y]
        for x in range(len(row)):
            cell = row[x]
            if makeKey(x, y) not in visitedCells:
                (area, perimeter) = findAreaPerim(x, y, grid, visitedCells, cell, 0)
                area += 1
                cost = area * perimeter
                total += cost
    print(total)
