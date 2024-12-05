import math

def check(numbers):
    noNoNumbers = []
    for i in range(len(numbers)):
        number = numbers[i]
        if number in noNoNumbers:
            return False
        if number in afters:
            beforesList = afters[number]
            noNoNumbers += beforesList
    return True

with open("input.txt", "r") as f:
    lines = f.readlines()
    afters = {}
    part = 0
    count = 0
    for line in lines:
        line = line.replace("\n", "")
        if line == "":
            part = 1
            continue

        if part == 0:
            numbers = line.split("|")
            before = numbers[0]
            after = numbers[1]
            if after in afters:
                afters[after].append(before)
            else:
                afters[after] = [before]
        else:
            numbers = line.split(",")
            wholeSuccess = False
            success = check(numbers)

            if not success:
                while not check(numbers):
                    knownBefores = {}
                    noNoNumbers = []
                    for i in range(len(numbers)):
                        number = numbers[i]
                        for known in knownBefores:
                            before = knownBefores[known]
                            if number in before[1]:
                                oldPos = before[0]
                                placeholder = numbers[oldPos]
                                numbers[oldPos] = numbers[i]
                                numbers[i] = placeholder
                        if number in afters:
                            beforesList = afters[number]
                            knownBefores[number] = (i, beforesList)
                toAdd = numbers[math.floor(len(numbers) / 2)]
                count += int(toAdd)
    print(count)
