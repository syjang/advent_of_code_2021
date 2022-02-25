data = set()
folds = []

with open('input.txt') as f:
    lines = f.readlines()
    for l in lines:
        
        if l.find('fold') != -1:
            tmp = l.split(' ')
            tmp = tmp[2].split('=')
            folds.append([tmp[0],int(tmp[1])])
            continue
        elif len(l) <= 1:
            continue

        tmp = l.split(',')
        x = int(tmp[0])
        y = int(tmp[1])
        data.add((x,y))

rightbound = 10e5
bottombound = 10e5


def PrintCount():
    count = 0 
    for d in data:
        if d[0] < rightbound and d[1] < bottombound:
            count +=1 
    print(count)

first = True 
for ff in folds:
    cmd = ff[0]
    val = ff[1]    
    idx = 0    
    idx2 = 1

    if ff[0] == 'y':
        idx = 1
        idx2 = 0
        bottombound = val
    else:
        idx = 0    
        idx2 = 1
        rightbound = val
    
    addSet = set()
    for d in data:
        if d[idx] > val:
            newidx = d[idx] - val
            newidx = val - newidx
            if newidx < 0:
                continue
            if ff[0] == 'y':
                addSet.add((d[0],newidx))
            else:
                addSet.add((newidx,d[1]))
    data.update(addSet)
    
    if first:
        PrintCount()
        first = False


for y in range(bottombound):
    stmp = ''
    for x in range(rightbound):
        if (x,y) in data:
            stmp +='#'
        else:
            stmp += '.'
    print(stmp)        
