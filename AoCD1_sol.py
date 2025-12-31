
dial = 50
password = 0
    
with open("AoCD1.txt", "r") as f:
    for line in f:
        direction = line[0]
        line = line.lstrip("LR")
        line = line.rstrip()
        num = int(line)

        if direction == "L":
            dial = dial - num
            while dial < 0:
                dial += 100
                    
        if direction == "R":
            dial = dial + num
            while dial > 99:
                dial -= 100
            
        if dial == 0:
            password += 1
                
print(password)
            
            
        
