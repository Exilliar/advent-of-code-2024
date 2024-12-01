with open("input.txt", "r") as f:
    list1 = []
    list2 = []
    for line in f.readlines():
        line = line.replace("\n", "")
        splitted = line.split("   ")
        list1.append(int(splitted[0]))
        list2.append(int(splitted[1]))
    list1.sort()
    list2.sort()

    total = 0

    for i in range(len(list1)):
        total += abs(list1[i] - list2[i])
    print(total)
