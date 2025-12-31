
with open("AoCD2.txt", "r") as f:
    line = f.readline()
    line = line.rstrip()
    ids = line.split(",")

invalidSum = 0

for ID in ids:
    numRange = ID.split("-")
    first = int(numRange[0])
    last = int(numRange[1])
    num = first
    
    while num <= last:
        numStr = str(num)
        numList = list(numStr)
        firstHalf = ""
        secHalf = ""
        
        if (len(numList)%2) != 0:
            num += 1
            continue
            
        i = 0
        while i < len(numList):
            if i < (len(numList)/2):
                firstHalf += numList[i]
            else:
                secHalf += numList[i]
            i +=1

        if firstHalf == secHalf:
            invalidSum += num
            
        num += 1
        
print(invalidSum)

        
            
        

