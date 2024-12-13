# fixed with help from q1-2.py, not used for q2, way too slow

import re
import math

def aSolve(aMod, y, k):
    return aMod + (y * k)
def bSolve(c, x, aMod, y, k):
    return (c - (x *(aMod + (y * k)))) / y

def genASolve(aMod, y):
    def solve(k):
        return aSolve(aMod, y, k)
    return solve
def genBSolve(c, x, aMod, y):
    def solve(k):
        return bSolve(c, x, aMod, y, k)
    return solve

def solve(x: int, y: int, c: int, limit: int):
    # this is an ax + by = c linear Diophantine equation where a, b, and c are known

    # step 1
    gcd = math.gcd(x, y)

    x = x / gcd
    y = y / gcd
    c = c / gcd
    if c % 1 != 0:
        return []

    # step 2
    # b = (c - xa)/y

    # step 3: ensure b is an integer
    cMod = c % y

    # thus congruence is: xa % c = cMod

    # step 4: simplify the congruence
    xMod = x % y
    # the congruence becomes xMod * a = cMod

    # step 5: solve for a
    # find the multiplicative inverse of xMod % y
    # inverse is found such that q * r == 1 (mod m), in this case we are looking for r such that xMod * r == 1 (mod y)
    r = 0
    if xMod == 0:
        r = 1
    else:
        while (xMod * r) % y != 1:
            r += 1

    # multiply through the inverse r
    aMod = r * cMod
    # simplify
    aMod = aMod % y
    # thus a = aMod + yk where k is any integer

    # step 6: solve for b

    # substitute a = aMod + yk into b = (c - xa)/y

    aFunc = genASolve(aMod, y)
    bFunc = genBSolve(c, x, aMod, y)

    aK = math.floor((-1 * aMod) / y)
    bK = math.floor(((c/x) - aMod) / y)
    startK = 0
    endK = 0
    if aK < bK:
        startK = aK
        endK = bK
    else:
        startK = bK
        endK = aK

    options = []
    for k in range(startK - 1, endK + 1):
        a = aFunc(k)
        b = bFunc(k)
        cost = (a * 3) + b
        if a <= limit and a >= 0 and b <= limit and b >= 0:
            options.append(((int(a), int(b)), int(cost)))

    return options

def calc(a, b, prize, limit):
    # solve for x
    xOptions = solve(a[0], b[0], prize[0], limit)

    # solve for y
    yOptions = solve(a[1], b[1], prize[1], limit)

    lowestCostMatch = -1
    for xOp in xOptions:
        xVals = xOp[0]
        for yOp in yOptions:
            yVals = yOp[0]
            if xVals[0] == yVals[0] and xVals[1] == yVals[1]:
                if lowestCostMatch == -1:
                    lowestCostMatch = yOp[1]
                elif lowestCostMatch > yOp[1]:
                    lowestCostMatch = yOp[1]

    return lowestCostMatch

with open("input.txt", "r") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]
    aLine = "Button A: X\+([0-9]*), Y\+([0-9]*)"
    bLine = "Button B: X\+([0-9]*), Y\+([0-9]*)"
    prizeLine = "Prize: X\=([0-9]*), Y\=([0-9]*)"

    currA = [0, 0]
    currB = [0, 0]
    currPrize = [0, 0]

    total = 0
    i = 0

    noSolution = []

    for line in lines:
        if line == "":
            cost = calc(currA, currB, currPrize, 100)
            if cost != -1:
                total += cost
            else:
                noSolution.append(f"i: {i}, prize: {currPrize[0]}, {currPrize[1]}")
            i += 1
        else:
            aSearch = re.search(aLine, line)
            bSearch = re.search(bLine, line)
            pSearch = re.search(prizeLine, line)
            if aSearch != None:
                groups = aSearch.groups()
                currA = [int(groups[0]), int(groups[1])]
            elif bSearch != None:
                groups = bSearch.groups()
                currB = [int(groups[0]), int(groups[1])]
            elif pSearch != None:
                groups = pSearch.groups()
                currPrize = [int(groups[0]), int(groups[1])]
    cost = calc(currA, currB, currPrize, 100)
    if cost != -1:
        total += cost
    print(total)
