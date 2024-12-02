# horrible solution

def isPassed(numbers):
    up = False
    down = False
    success = True
    curr = int(numbers[0])
    for i in range(1, len(numbers)):
        nxt = int(numbers[i])
        if curr < nxt and abs(curr - nxt) <= 3 and down == False:
            up = True
            curr = nxt
        elif curr > nxt and abs(curr - nxt) <= 3 and up == False:
            down = True
            curr = nxt
        else:
            success = False
            break
    return success

with open("input.txt", "r") as f:
    passed = 0
    for line in f.readlines():
        line = line.replace("\n", "")
        splitted = line.split(" ")
        success = isPassed(splitted)
        if success != True:
            oldList = [l for l in splitted]
            for i in range(len(splitted)):
                splitted = [s for s in oldList]
                splitted.pop(i)
                success = isPassed(splitted)
                if success:
                    break
        if success:
            passed += 1
    print(passed)
