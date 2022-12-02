with open('day1.txt') as f:
    lines = f.readlines()
    listOfLists = []
    tempList = []
    for line in lines:
        if line == '\n':
            listOfLists.append(tempList)
            tempList = []
        else:
            tempList.append(int(line.strip()))
    calorieList = []
    for elf in listOfLists:
        calorieList.append(sum(elf))
    calorieList.sort()
    Part2 = calorieList[-1] + calorieList[-2] + calorieList[-3]
    print(f"Part 1: {calorieList[-1]}")
    print(f"Part 2: {Part2}")
