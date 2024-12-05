import math

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
            success = True
            noNoNumbers = []
            for i in range(len(numbers)):
                number = numbers[i]
                if number in noNoNumbers:
                    success = False
                    break
                if number in afters:
                    beforesList = afters[number]
                    noNoNumbers += beforesList

            if success == True:
                toAdd = numbers[math.floor(len(numbers) / 2)]
                count += int(toAdd)
    print(count)
