def runRules(number: int) -> list:
    if number == 0:
        return [1]
    elif len(str(number)) % 2 == 0:
        strNumber = str(number)
        firstpart, secondpart = strNumber[:len(strNumber)//2], strNumber[len(strNumber)//2:]
        return [int(firstpart), int(secondpart)]
    else:
        return [number * 2024]

with open("input.txt", "r") as f:
    numbers = f.read().replace("\n", "").split(" ")
    blinks = 25
    count = 0
    for n in numbers:
        arr = [n]
        for blink in range(blinks):
            for i in range(len(arr)):
                changed = runRules(int(arr[i]))
                arr[i] = changed[0]
                if len(changed) > 1:
                    arr.append(changed[1])
        count += len(arr)
    print(count)
