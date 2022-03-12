

data = [] 
with open('input.txt') as f:
    lines = f.readlines()
    
    
    for l in lines:
        tmp = [int(s) for s in l if s != '\n']
        data.append(tmp)


rows = len(data)
cols = len(data[0])

sums = [[0 for x in range(cols)] for y in range(rows)] 

# y,x
stt = {0,0}
finish = {cols-1,rows-1}
    

for i in range(cols+1):
    for c in range(i):
        for r in range(i):
            y,x = r,c
            cur = data[y][x]

            if x==0 and y ==0:
                continue

            a,b,a2,b2= 10000,10000,10000,10000
            if y >= 1:
                if sums[y-1][x] !=0:
                    a = sums[y-1][x]
            if x >= 1:
                if sums[y][x-1] !=0:
                    b = sums[y][x-1]        
            if x < cols -1:
                if sums[y][x+1] !=0:
                    a2 = sums[y][x+1]        
            if y < rows -1:
                if sums[y+1][x] !=0:
                    b2 = sums[y+1][x]

            minV = min(min(a,b),min(a2,b2))
            if minV == 10000 :
                sums[y][x] = cur
                continue        

            count = minV + cur

            if sums[y][x] == 0:
                sums[y][x] = count
            elif sums[y][x] > count:
                sums[y][x] = count

print(sums[cols-1][rows-1])
   
sums = [[0 for x in range(cols*5)] for y in range(rows*5)] 

for i in range((cols) *5 + 1):
    for c in range(i):
        for r in range(i):
            y,x = r,c
            addr = r //rows
            addc = c //cols
            cur = data[y%rows][x%cols] + addr + addc           
            if cur > 9:
                cur -= 9

            if x==0 and y ==0:
                continue

            a,b,a2,b2= 10000,10000,10000,10000
            if y >= 1:
                if sums[y-1][x] !=0:
                    a = sums[y-1][x]
            if x >= 1:
                if sums[y][x-1] !=0:
                    b = sums[y][x-1]        
            if x < cols -1:
                if sums[y][x+1] !=0:
                    a2 = sums[y][x+1]        
            if y < rows -1:
                if sums[y+1][x] !=0:
                    b2 = sums[y+1][x]

            minV = min(min(a,b),min(a2,b2))
            if minV == 10000 :
                sums[y][x] = cur
                continue        

            count = minV + cur

            if sums[y][x] == 0:
                sums[y][x] = count
            elif sums[y][x] > count:
                sums[y][x] = count


print(sums[cols*5-1][rows*5-1])