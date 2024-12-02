with open("input.txt", "r") as f:
    passed = 0
    for line in f.readlines():
        up = False
        down = False
        success = True
        numbers = line.split(" ")
        curr = int(numbers[0])
        for i in range(1, len(numbers)):
            nxt = int(numbers[i])
            if curr < nxt and curr >= nxt - 3 and down == False:
                up = True
                curr = nxt
            elif curr > nxt and curr <= nxt + 3 and up == False:
                down = True
                curr = nxt
            else:
                success = False
                break
        if success:
            passed += 1
    print(passed)

