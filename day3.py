import os 

with open('input.txt') as f:
    l = f.readlines()
    data = l

cols = len(data[0]) -1
ret = [0] * cols

rows = len(data)
for d in data :
    for i in range(cols):
        if d[i] == '1':
            ret[i] += 1



for i in range(len(ret)):
    if ret[i] > rows//2 :
        ret[i] = '1'
    else:
        ret[i] = '0'

ret2 = []
for i,s in enumerate(ret):
    if s=='0':
        ret2.append('1')
    else: 
        ret2.append('0')

tt = ""
tt2 = ''
tt = tt.join(ret)
tt2 = tt2.join(ret2)

a = int(tt,2)
b = int(tt2,2)

print(a*b)




import copy
# anw2 
ogr = [0] * cols
csr = [0] * cols

oriData = copy.deepcopy(data)

for i in range(cols):
    a =[]
    b =[]
    for d in data :    
        if d[i] == '1':
            a.append(d)
        else:
            b.append(d)
    
    if len(a) >= len(b):
        data = a
    else:
        data = b 
    
ogr = data
data = copy.deepcopy(oriData)

for i in range(cols):
    a =[]
    b =[]

    if len(data) == 1:
        break
    for d in data :    
        if d[i] == '1':
            a.append(d)
        else:
            b.append(d)
    
    if len(a) >= len(b):
        data = b
    else:
        data = a 
    
csr = data 


tt = ""
tt2 = ''
tt = tt.join(ogr)
tt2 = tt2.join(csr)

a = int(tt,2)
b = int(tt2,2)

print(a*b)
       