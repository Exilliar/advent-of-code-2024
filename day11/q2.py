def runRules(number: int) -> list:
    if number == 0:
        return [1]
    elif len(str(number)) % 2 == 0:
        strNumber = str(number)
        firstpart, secondpart = strNumber[:len(strNumber)//2], strNumber[len(strNumber)//2:]
        return [int(firstpart), int(secondpart)]
    else:
        return [number * 2024]

visitedNumbers = {}

def rRunRules(number: int, blinks: int):
    numberKey = f"{str(number)},{blinks}"
    if numberKey in visitedNumbers:
        return visitedNumbers[numberKey]
    if (blinks == 0):
        visitedNumbers[numberKey] = 1
        return 1
    else:
        changed = runRules(number)
        output = rRunRules(changed[0], blinks - 1)
        if len(changed) > 1:
            out2 = rRunRules(changed[1], blinks - 1)
            output += out2
        visitedNumbers[numberKey] = output
        return output

with open("input.txt", "r") as f:
    numbers = f.read().replace("\n", "").split(" ")
    blinks = 75
    count = 0

    for n in numbers:
        count += rRunRules(int(n), blinks)
    print(count)
