from typing import Callable, Tuple, List

def up(x: int, y: int):
    return (x, y-1, "up")
def right(x: int, y: int):
    return (x+1, y, "right")
def down(x: int, y: int):
    return (x, y+1, "down")
def left(x: int, y: int):
    return (x-1, y, "left")

def moveFunc(func: Callable[[int, int], Tuple[int, int, str]], x: int, y: int, maxX: int, maxY: int, currVal: int, grid: List[List[str]]) -> Tuple[bool, Tuple[int, int]]:
    x, y, _ = func(x, y)
    if x >= 0 and x < maxX and y >= 0 and y < maxY:
        if grid[y][x] == str(currVal + 1):
            return (True, (x, y))
    return (False, (x, y))

def findPath(x: int, y: int, maxX: int, maxY: int, grid: List[List[str]]) -> Tuple[bool, List[Tuple[int, int]]]:
    if grid[y][x] == ".":
        return (False, [])
    val = int(grid[y][x])
    if val == 9:
        return (True, [(x, y)])

    outputs: list[tuple[int, int]] = []

    pathUp = None
    moveUp = moveFunc(up, x, y, maxX, maxY, val, grid)
    if moveUp[0]:
        pathUp = findPath(moveUp[1][0], moveUp[1][1], maxX, maxY, grid)
        if pathUp[0] == True:
            outputs += pathUp[1]

    pathRight = None
    moveRight = moveFunc(right, x, y, maxX, maxY, val, grid)
    if moveRight[0]:
        pathRight = findPath(moveRight[1][0], moveRight[1][1], maxX, maxY, grid)
        if pathRight[0] == True:
            outputs += pathRight[1]

    pathDown = None
    moveDown = moveFunc(down, x, y, maxX, maxY, val, grid)
    if moveDown[0]:
        pathDown = findPath(moveDown[1][0], moveDown[1][1], maxX, maxY, grid)
        if pathDown[0] == True:
            outputs += pathDown[1]

    pathLeft = None
    moveLeft = moveFunc(left, x, y, maxX, maxY, val, grid)
    if moveLeft[0]:
        pathLeft = findPath(moveLeft[1][0], moveLeft[1][1], maxX, maxY, grid)
        if pathLeft[0] == True:
            outputs += pathLeft[1]
    if len(outputs) > 0:
        return (True, outputs)

    return (False, [])

with open("input.txt", "r") as f:
    grid = [list(line.replace("\n", "")) for line in f.readlines()]
    maxY = len(grid)
    maxX = len(grid[0])
    count = 0

    for y in range(len(grid)):
        row = grid[y]
        for x in range(len(row)):
            val = row[x]
            if val == "0":
                paths = findPath(x, y, maxX, maxY, grid)
                if paths[0] == True:
                    count += len(paths[1])
    print(count)

