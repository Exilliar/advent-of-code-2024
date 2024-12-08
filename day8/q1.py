with open("input.txt", "r") as f:
    lines = f.readlines()
    rows = len(lines)
    cols = len(lines[0].replace("\n", ""))
    frequencies: dict[str, list[tuple[int, int]]] = {} # tuple(x, y)
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            val = lines[y][x]
            if val != "." and val != "\n":
                if val in frequencies:
                    frequencies[val].append((x, y))
                else:
                    frequencies[val] = [(x, y)]

    antinodes: dict[str, bool] = {} # str(x,y)
    for frequency in frequencies:
        nodes = frequencies[frequency]
        for i in range(len(nodes) - 1):
            currNode = nodes[i]
            for x in range(i + 1, len(nodes)):
                nextNode = nodes[x]
                heightChange = currNode[1] - nextNode[1]
                widthChange = currNode[0] - nextNode[0]
                anti1 = (currNode[0] + widthChange, currNode[1] + heightChange)
                anti2 = (nextNode[0] - widthChange, nextNode[1] - heightChange)
                if anti1[0] >= 0 and anti1[0] < cols and anti1[1] >= 0 and anti1[1] < rows:
                    antinodes[f"{anti1[0]},{anti1[1]}"] = True
                if anti2[0] >= 0 and anti2[0] < cols and anti2[1] >= 0 and anti2[1] < rows:
                    antinodes[f"{anti2[0]},{anti2[1]}"] = True
    
    print(len(antinodes))
