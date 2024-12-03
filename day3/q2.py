import re

def mult(command: str):
    numbers = command[4:][:-1].split(",")
    return int(numbers[0]) * int(numbers[1])

regex = "(mul\([0-9]+,[0-9]+\))|(do\(\))|(don't\(\))"

with open("input.txt", "r") as f:
    total = 0
    calc = True
    for line in f.readlines():
        matches = re.findall(regex, line)
        lineTotal = 0
        for match in matches:
            if match[1] == "do()":
                calc = True
            elif match[2] == "don't()":
                calc = False
            elif calc:
                lineTotal += mult(match[0])
        total += lineTotal
    print(total)
