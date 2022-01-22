
with open('input.txt') as f:
    l = f.readlines()
    data = []
    for s in l:
        s = s.replace(' -> ',',')
        d = s.split(',')
        d = [ int(s) for s in d]
        data.append(d)

# x1,y1,x2,y2
xm = 1000 
ym = 1000

xymap = [ [0]*(xm+1) for i in range(ym +1)]

for d in data:
    x1,y1,x2,y2 = d[0],d[1],d[2],d[3]

    sttX = min(x1,x2)
    endX = max(x1,x2)

    sttY = min(y1,y2)
    endY = max(y1,y2)

    if sttX != endX and sttY != endY:
        continue

    for x in range(sttX,endX+1):
        for y in range(sttY,endY+1):
            xymap[x][y] += 1

count = 0
for x in range(xm):
    for y in range(ym):
        if xymap[x][y] > 1:
            count +=1

print(count)


xymap = [ [0]*(xm+1) for i in range(ym +1)]

for d in data:
    x1,y1,x2,y2 = d[0],d[1],d[2],d[3] 
    sttX = min(x1,x2)
    endX = max(x1,x2)

    sttY = min(y1,y2)
    endY = max(y1,y2)   

    if sttX != endX and sttY != endY:
        x = x1
        y = y1
        
        sumX = 1
        sumY = 1
        if x2 < x1:
            sumX = -1
        if y2 < y1:
            sumY = -1

        while y != y2 and x != x2 :            
            xymap[x][y] += 1
            x += sumX
            y += sumY 
        
        xymap[x][y] += 1
            
    else:        
        for x in range(sttX,endX+1):
            for y in range(sttY,endY+1):
                xymap[x][y] += 1

count = 0
for x in range(xm):
    for y in range(ym):
        if xymap[x][y] > 1:
            count +=1

print(count)