import math
from typing import Callable

def add(a: int, b: int) -> int:
    return a + b
def mult(a: int, b: int) -> int:
    return a * b

availableCalcs = [add, mult]

def count(availablePos: int, base: int) -> list[list[int]]:
    lines = []
    for i in range(int(math.pow(base, availablePos))):
        line = [0 for x in range(availablePos)]
        target = i
        currPos = availablePos - 1
        for x in range(availablePos):
            while line[x] < base:
                addVal = int(math.pow(base, currPos))
                if addVal <=  target:
                    line[x] += 1
                    target -= addVal
                else:
                    break
            currPos -= 1
        lines.append(line)
    return lines

def calc(calcList: list[int], numbers: list[int], availableCalcs: list[Callable[[int, int], int]], maxVal: int) -> int:
    currentCalcListPos = 0
    currVal = numbers[0]
    for i in range(1, len(numbers)):
        currVal = availableCalcs[calcList[currentCalcListPos]](currVal, numbers[i])
        currentCalcListPos += 1
        if currVal > maxVal:
            return (False, currVal)
    return (True, currVal)

with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        [target, numbers] = line.split(": ")
        target = int(target)
        numbers = [int(number) for number in numbers.split(" ")]
        availablePos = len(numbers) - 1
        calcLists = count(availablePos, len(availableCalcs))
        for c in calcLists:
            result = calc(c, numbers, availableCalcs, target)
            if result[0] == True and result[1] == target:
                total += target
                break
    print(total)
