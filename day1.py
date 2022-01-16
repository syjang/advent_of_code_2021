import os 

with open('input.txt') as f:
    l = f.readlines()
    data = [int(s) for s in l]

count = 0
ex = data[0]
for i in range(1,len(data)):
    if ex < data[i]:
        count += 1

    ex = data[i]


print(count)




with open('input2.txt') as f:
    l = f.readlines()
    data = [int(s) for s in l]


count =0 
stt = 0
end = 3
while end+1 <= len(data):
    ex = sum(data[stt:end])
    next = sum(data[stt+1:end+1])
    if next > ex:
        count +=1
    
    stt +=1 
    end +=1
    


print(count)

