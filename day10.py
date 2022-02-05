

with open('input.txt') as f:
    data = f.readlines()


'('
')'
'['
']'
'{'
'}'
'<'
'>'
from collections import deque


ret = 0
ret2= []

for ch in data:
    q = deque()
    bad = False
    for c in ch:
        if c in ['(', '[', '{', '<']:
            q.append(c)
        elif c==')':
            if q[-1] != '(':
                ret += 3
                bad = True
                break
            else:
                q.pop()
        elif c==']':
            if q[-1] != '[':
                ret += 57
                bad = True
                break
            else:
                q.pop()
        elif c=='}':
            if q[-1] != '{':
                ret += 1197
                bad = True
                break
            else:
                q.pop()
        elif c=='>':
            if q[-1] != '<':
                ret += 25137
                bad = True
                break
            else:
                q.pop()
    if not bad:
        point = 0
        pmap = {'(': 1, '[': 2, '{': 3, '<': 4}
        for c in reversed(q):
            point = point*5 + pmap[c]
        ret2.append(point)
       
print(ret)
ret2.sort()
print(ret2[len(ret2)//2])


