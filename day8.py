from numpy import append


with open('input.txt') as f:
    lines = f.readlines()

    inputs = []
    outputs = []
    for l in lines:
        l = l.split('|')
        first = l[0].split(' ')    
        first = [ s for s in first]    
        inputs.append(first)
        out = l[1].split(' ')
        out = [ s.replace('\n','') for s in out ]    
        outputs.append(out)




count = 0 
for idx, inp in enumerate(inputs) :
    out = outputs[idx]
    ct = 0
    for o in out:
        if len(o) == 2 or len(o) ==3 or len(o) == 4 or len(o) == 7:
            ct +=1 

    count += ct

print(count)
    
# a,b,c,d,e,f,g
# 0,1,2,3,4,5,6
segment =['']*7
val = ['']*10
ret = 0
count = 0 
for idx, inp in enumerate(inputs) :               
    # find value
    one = ''
    for c in inp:
        if len(c) == 2:
            val[1] = c
            one = c            
        elif len(c) == 3:
            val[7] = c
        elif len(c) == 4:
            val[4] = c
        elif len(c) == 7:
            val[8] = c 
    
    # find segment 0
    for c in inp:
        if len(c) == 3:
            val[7] = c
            inp.remove(c)
            c = c.replace(one[0],'')
            c = c.replace(one[1],'')
            segment[0] = c       
            break
    
    #find segment 6
    # 9 - 4
    for c in inp:
        if len(c) == 6:
            tmp = c 
                        
            c = c.replace(segment[0],'')

            for c in val[4]:
                c = c.replace(c,'')

            if len(c) != 1:
                continue
            
            val[9] = tmp
            segment[6] = c[0]
            break 
    
    #find segment 4
    # 8-9
    tmp = val[8]
    for c in val[9]:
        tmp = tmp.replace(c,'')
    
    segment[4] = tmp[0]

    # find segment 2
    # 9-5
    for c in inp:
        if len(c) == 5:
            tmp = val[9]
            for cc in c:
                tmp = tmp.replace(cc,'')
            
            if len(tmp) ==1 and tmp in one:
                segment[2] = tmp[0]
                val[5] = c
                t = one
                t = t.replace(tmp[0],'')
                segment[5] = t[0]
            elif len(tmp) ==1:
                segment[1] = tmp[0]
                val[3] = c
                
    # find segment 3
    # 3 -1 seg[0] seg[6]
    tmp = val[3]
    for c in val[1]:
        tmp = tmp.replace(c,'')
    tmp = tmp.replace(segment[0],'')
    tmp = tmp.replace(segment[6],'')

    segment[3] = tmp

    s = []
    s.append([segment[0],segment[1],segment[2],segment[4],segment[5],segment[6]]) # 0
    s.append([segment[2],segment[5]]) #1
    s.append([segment[0],segment[2],segment[3],segment[4],segment[6]])#2
    s.append([segment[0],segment[2],segment[3],segment[5],segment[6]])#3
    s.append([segment[1],segment[2],segment[3],segment[5]])#4
    s.append([segment[0],segment[1],segment[3],segment[5],segment[6]])#5
    s.append([segment[0],segment[1],segment[3],segment[4],segment[5],segment[6]])#6
    s.append([segment[0],segment[2],segment[5]])#7
    s.append([segment[0],segment[1],segment[2],segment[3],segment[4],segment[5],segment[6]])#8
    s.append([segment[0],segment[1],segment[2],segment[3],segment[5],segment[6]])#9

    

    out = outputs[idx]
    tmp = ''
    for o in out:
        if len(o) ==0:
            continue
        if len(o) ==2:
            tmp += '1'
        elif len(o) ==3:
            tmp += '7'
        elif len(o) == 4:
            tmp += '4'
        elif len(o) == 7:
            tmp += '8'
        else:
            for idx, ss in enumerate(s):
                listToStr = ''.join([str(elem) for elem in ss])
                if len(o) == len(listToStr):
                    if sorted(o) == sorted(listToStr):
                        tmp += str(idx)
            
            
    # print(tmp)

    ret += int(tmp,10)

print(ret)




    