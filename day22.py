from collections import Counter
import re

from itertools import product

with open('input3.txt') as f:
    data = f.readlines()

def part1():
    cubeset = set()
    for q in data:
        tmp = q.split(' ')
        on = True if tmp[0] == 'on' else False
        tmp = tmp[1].split(',')
        x = re.findall(r'[-]?\d+',tmp[0][2:])
        x = [int(v) for v in x]
        y = re.findall(r'[-]?\d+',tmp[1][2:])
        y = [int(v) for v in y]
        z = re.findall(r'[-]?\d+',tmp[2][2:])
        z = [int(v) for v in z]

        if (x[0] < -50 and x[1] < -50 ) or (x[0] >50 and x[1] > 50):
                continue

        if (y[0] < -50 and y[1] < -50 ) or (y[0] >50 and y[1] > 50):
            continue

        if (z[0] < -50 and z[1] < -50 ) or (z[0] >50 and z[1] > 50):
            continue


        all = list(product(range(x[0],x[1]+1),range(y[0],y[1]+1),range(z[0],z[1]+1)))

        if on:             
            for v in all:
                cubeset.add(v)

        else:
            for v in all:
                if v in cubeset:
                    cubeset.remove(v)


    print(len(cubeset))


def part2():

    counter = 0 
    cubes = Counter()

    def getduple(x,y,z,x_,y_,z_ ):
        if x[0] == x_[0] and x[1] == x_[1] and y[0] == y_[0] and y[1] == y_[1] and z[0] == z_[0] and z[1] == z_[1]:
            return [],[],[]

        if  ( x[0] <= x_[1] and x[1] >= x_[0]) and ( y[0] <= y_[1] and y[1] >= y_[0]) and ( z[0] <= z_[1] and z[1] >= z_[0]):
            xtmp = [x_[0],x_[1],x[0],x[1]]
            xtmp.sort()
            ytmp = [y_[0],y_[1],y[0],y[1]]
            ytmp.sort()
            ztmp = [z_[0],z_[1],z[0],z[1]]
            ztmp.sort()                            
            return xtmp[1:3],ytmp[1:3],ztmp[1:3]
        
        else:
            return [],[],[]

    for q in data:
        tmp = q.split(' ')
        on = True if tmp[0] == 'on' else False
        tmp = tmp[1].split(',')
        x = re.findall(r'[-]?\d+',tmp[0][2:])
        x = [int(v) for v in x]
        y = re.findall(r'[-]?\d+',tmp[1][2:])
        y = [int(v) for v in y]
        z = re.findall(r'[-]?\d+',tmp[2][2:])
        z = [int(v) for v in z]

        if on:          
            cubes[tuple(map(int,(x+y+z)))] += 1
        
        updateCounter = Counter()
        for area, val in cubes.items():
            x_,y_,z_ = getduple(area[:2],area[2:4],area[4:6],x,y,z)
            if len(x_) != 0:
                updateCounter[tuple(map(int,(x_+y_+z_)))] -= val

        cubes.update(updateCounter)


    
    for cube , value in cubes.items():
        xtmp = cube[:2]
        ytmp = cube[2:4]
        ztmp = cube[4:6]
        counter += ((abs(xtmp[1] - xtmp[0]) + 1) * (abs(ytmp[1] - ytmp[0]) + 1) * (abs(ztmp[1] - ztmp[0]) + 1)) * value  
    
    print(counter)


part2()

