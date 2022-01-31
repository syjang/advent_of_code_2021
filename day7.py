with open('input.txt') as f:
    l = f.read()
    l = l.split(',')
    data = [int(s) for s in l]


ret = 10e6
for i in range(max(data)*2):
    sum = 0 
    for v in data:
        sum += abs(i-v)

    ret = min(ret,sum)

print(ret)

ret = 10e10
tmap = {} 
for i in range(max(data)*2):
    sum = 0 
    for v in data:
        tmp = abs(i-v)
        tsum = 0
        if tmp in tmap:
            tsum = tmap[tmp]
        else:
            for j in range(1,tmp+1):
                tsum += j
            tmap[tmp] = tsum

        sum += tsum

    ret = min(ret,sum)

print(ret)

