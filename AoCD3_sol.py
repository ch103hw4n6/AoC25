with open("AoCD3.txt", "r") as f:
    jolt = 0
    total = 0
    for line in f:
        firstMax = 0
        line = line.rstrip()
        numList = list(line)
        numList = [int(x) for x in numList]
        
        maxOne = max(numList)
        index = numList.index(maxOne)

##        if numList.index(maxOne) == (len(numList)-1):
##            newList = numList[0:-1]
##            maxOne = max(newList)
##            index = newList.index(maxOne)
            
        for i in range(index+1):
            numList[i] = 0

        maxTwo = max(numList)

        jolt = maxOne*10 + maxTwo
        total += jolt
        
print(total)

        
        
