import os 

with open('input.txt') as f:
    l = f.readlines()
    data = [ s.split(' ') for s in l]

# x, y 
pos = [0,0]
for d in data:
    cmd = d[0][0]
    v = int(d[1])
    if cmd == 'f':
        pos[0] += v
    elif cmd == 'd':
        pos[1] += v
    elif cmd =='u':
        pos[1] -= v

#anw 1
print(pos[0] *pos[1])
    

aim = 0 
pos = [0,0]
for d in data:
    cmd = d[0][0]
    v = int(d[1])
    if cmd == 'f':
        pos[0] += v
        pos[1] += aim*v
    elif cmd == 'd':
        aim += v        
    elif cmd =='u':
        aim -= v
        
print(pos[0] *pos[1])
