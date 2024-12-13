# kinda feels like cheating cuz got maths from reddit, credit to https://www.reddit.com/r/adventofcode/comments/1hd7irq/2024_day_13_an_explanation_of_the_mathematics/

import re

def calc(a, b, prize, limit):
    A = (prize[0] * b[1] - prize[1] * b[0]) / (a[0] * b[1] - a[1] * b[0])
    B = (a[0] * prize[1] - a[1] * prize[0]) / (a[0] * b[1] - a[1] * b[0])
    if A % 1 == 0 and B % 1 == 0 and A <= limit and B <= limit:
        return (A * 3) + B
    return -1

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
