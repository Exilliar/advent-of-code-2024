import re

def mul(command: str):
    numbers = command[4:][:-1].split(",")
    return int(numbers[0]) * int(numbers[1])

regex = "mul\([0-9]+,[0-9]+\)"

with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        matches = re.findall(regex, line)
        lineTotal = sum([mul(match) for match in matches])
        total += lineTotal
    print(total)
