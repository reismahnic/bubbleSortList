def bubbleSort(sortList):
    for passnum in range(len(sortList)-1,0,-1):
        for i in range(passnum):
            if sortList[i]>sortList[i+1]:
                temp = sortList[i]
                sortList[i] = sortList[i+1]
                sortList[i+1] = temp

sortList = [67, 45, 2, 13, 1, 998]
bubbleSort(sortList)
print(sortList)

sortList = [89, 23, 33, 45, 10, 12, 45, 45, 45]
bubbleSort(sortList)
print(sortList)
