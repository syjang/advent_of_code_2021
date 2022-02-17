from collections import defaultdict

data = defaultdict(set)
with open('input.txt') as f:
    lines = f.readlines()
    for l in lines:
        first = l.split('-')[0]
        second = l.split('-')[1]
        second = second.replace('\n','')

        data[first].add(second)
        data[second].add(first)


start = 'start'
end = 'end'

paths = list()

def go(node,path):    
    global paths
    if node == "end":
        paths.append(path)
        return
    for v in data[node]:
        if v == "start":
            continue
        if v not in path or v.isupper() or (not [n for n in path if n.islower() and path.count(n) > 1]):
            new_path = path.copy()
            new_path.append(v)
            go(v, new_path)

t = [start]
go(start,t)



print(len(paths))
    




        