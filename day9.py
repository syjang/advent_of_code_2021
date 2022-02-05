

heightmap = []

with open('input.txt') as f:
    lines = f.readlines()
    for l in lines:
        l = [ int(c) for c in l if c != '\n']
        heightmap.append(l)

rows = len(heightmap)
cols = len(heightmap[0])


ret =[]

for r in range(rows):
    for c in range(cols):
        up,down,left,right = 10,10,10,10
        cen = heightmap[r][c]
        if r + 1 < rows:
            right = heightmap[r+1][c]
        if r - 1 < rows:
            left = heightmap[r-1][c]
        if c + 1 < cols:
            up = heightmap[r][c+1]
        if c - 1 < cols:
            down = heightmap[r][c-1]

        if cen < up and cen < down and cen < left and cen < right:
            ret.append(cen + 1)

print(sum(ret))

# anw2
from collections import deque
ret =[]
adr = [-1,0,1,0]
adc = [0,1,0,-1]
visit = [[False]*cols for i in range(rows)]
for r in range(rows):
    for c in range(cols):
        cen = heightmap[r][c]
        if cen != 9 and visit[r][c] ==False:
            size = 0
            queue = deque()
            queue.append((r,c))
            while queue:
                (r,c) = queue.popleft()
                if visit[r][c]:
                    continue
                visit[r][c] = True
                size += 1
                for d in range(4):
                    rr = r+adr[d]
                    cc = c+adc[d]
                    if 0<=rr<rows and 0<=cc<cols  and heightmap[rr][cc]!=9:
                        queue.append((rr,cc))
            ret.append(size)

ret.sort(reverse=True)



print(ret[0]*ret[1]*ret[2])