
data = []
with open('input.txt') as f:
    lines = f.readlines()
    for l in lines:
        tmp = [int(c) for c in l if c !='\n' ]
        data.append(tmp)

rd = [1,1,0,-1,-1,0,-1,1]
cd = [0,1,1,0,-1,-1,1,-1]

rows = 10
cols = 10
n = 100

def addadjacent(r,c,tmpData):
    for j in range(8):
        nr = r + rd[j]
        nc = c + cd[j]
        if 0 <= nr < rows and 0 <= nc < cols and data[nr][nc] != 0:
            tmpData[nr][nc] += 1            
            if tmpData[nr][nc] > 9:
                tmpData[nr][c] = 0
            


flashcount = 0
for i in range(100000):
    
    for r in range(rows):
        for c in range(cols):
            data[r][c] += 1    

    find = True
    while find:
        tdata = [[ 0 for x in range(10)] for y in range(10)]
        find = False
        for r in range(rows):
            for c in range(cols):
                if data[r][c] > 9:
                    data[r][c] = 0
                    find = True
                    addadjacent(r,c,tdata)
        
        for r in range(rows):
            for c in range(cols):
                if data[r][c] !=0 :
                    data[r][c] += tdata[r][c]
    
    allflash = 0
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == 0:
                allflash += 1
                flashcount += 1
    if allflash == 100:
        print("anw2 ", i+1)
        break

    if i == 99:
        print("anw1" ,flashcount)

# print(flashcount)

                
                    
            



