# again, slow, but working

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
    currId -= 1

    while currId > 0:
        print(currId)
        while unfragged[i] != str(currId):
            i -= 1
        endPos = i
        while unfragged[i] == str(currId):
            i -= 1
        startPos = i
        length = endPos - startPos
        dotPos = 0
        startDotPos = 0
        endDotPos = 0
        dotsLength = 0
        posFound = False
        while posFound != True and dotPos < i:
            startDotPos = 0
            while unfragged[dotPos] != ".":
                dotPos += 1
            if dotPos > i + 1:
                break
            startDotPos = dotPos
            while unfragged[dotPos] == ".":
                dotPos += 1
            if dotPos > i + 1:
                break
            endDotPos = dotPos
            dotsLength = endDotPos - startDotPos
            if dotsLength >= length:
                posFound = True
        if posFound:
            for x in range(startPos + 1, endPos + 1):
                unfragged[x] = "."
            for x in range(startDotPos, startDotPos + length):
                unfragged[x] = str(currId)

        currId -= 1

    checkSum = 0
    for i in range(len(unfragged)):
        if unfragged[i] != ".":
            checkSum += int(unfragged[i]) * i
    print(checkSum)
