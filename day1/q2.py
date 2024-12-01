with open("input.txt", "r") as f:
    list1 = []
    list2 = []
    for line in f.readlines():
        line = line.replace("\n", "")
        splitted = line.split("   ")
        list1.append(int(splitted[0]))
        list2.append(int(splitted[1]))

    score = 0
    for a in list1:
        itemTotal = 0
        for b in list2:
            if b == a:
                itemTotal += 1
        score += itemTotal * a

    print(score)