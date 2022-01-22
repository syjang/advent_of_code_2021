

with open('input.txt') as f:
    l = f.readlines()
    ss = l[0].split(',')
    data = [int(s) for s in ss]


cmap = [0]*9

for d in data:
    cmap[d] += 1

# 80 -> 256
for i in range(256):
    tmp = cmap[0]     
    for j in range(1,9):        
        cmap[j-1] = cmap[j]
    cmap[8] = tmp   
    cmap[6] += tmp
    
    
print(sum(cmap))


