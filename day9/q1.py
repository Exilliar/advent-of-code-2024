# _real_ slow, but works

def checkIncomplete(unfragged: list) -> bool:
    foundDot = False
    for f in unfragged:
        if f == ".":
            foundDot = True
        if foundDot and f != ".":
            return True
    return False

with open("input.txt", "r") as f:
    line = list(f.read().replace("\n", ""))
    currId = 0
    unfragged = []
    saving = True
    for c in line:
        charToAdd = ""
        if saving == True:
            charToAdd = str(currId)
            currId += 1
        else:
            charToAdd = "."
        saving = not saving
        for i in range(int(c)):
            unfragged.append(charToAdd)

    i = len(unfragged) - 1
    while checkIncomplete(unfragged):
        print("loop")
        while unfragged[i] == ".":
            i -= 1
        dotPos = 0
        while unfragged[dotPos] != ".":
            dotPos += 1
        placeholder = unfragged[dotPos]
        unfragged[dotPos] = unfragged[i]
        unfragged[i] = placeholder

    checkSum = 0
    for i in range(len(unfragged)):
        if unfragged[i] == ".":
            break
        checkSum += int(unfragged[i]) * i
    print(checkSum)
