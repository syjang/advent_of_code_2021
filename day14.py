from collections import Counter


data = dict()


with open('input.txt') as f:
    lines = f.readlines()
    temp = lines[0]

    for a in lines[2:]:
        a = a.split(' ')
        a1 = a[0]
        a2 = a[2].replace('\n','')
        data[a1] = a2


temp = temp.replace('\n','')
startStr = temp

for i in range(10):
    newstr = ''

    for j in range(len(startStr)-1):
        s = startStr[j:j+2]
        newstr += startStr[j] + data[s]
        
    newstr += startStr[-1]
    startStr = newstr   
    

slist = [c for c in startStr]

tmp = Counter(slist)
tmp = tmp.most_common()
print(tmp[0][1]-tmp[-1][1])



pairs = Counter([temp[i : i + 2] for i in range(len(temp) - 1)])


for _ in range(40):
    newPairs = Counter()
    for p, v in pairs.items():
        if p in data:
            c = data[p]
            newPairs[p[0] + c] += v
            newPairs[c + p[1]] += v
        else:
            newPairs[p] += pairs[p]
    pairs = newPairs


count = Counter()
for p, v in pairs.items():
    count[p[0]] += v
count[temp[-1]] += 1

count = count.most_common()
print(count[0][1] - count[-1][1])