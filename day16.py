from functools import reduce
def convertHexToBin(value : str) -> str:
    return bin(int(value,16))[2:].zfill(4)



with open('input.txt') as f:
    temp = f.read()
    oridata = [convertHexToBin(s) for s in temp]    
    data = ''
    for s in oridata:
        data += s

tPos = 0



versionSum = 0
def parsePacket(packet : list ,maxCount:int = 100000000 ,clist:list = []):    
    global versionSum
    global tPos
    pos = 0
    i = 0    
    while pos < len(packet) - 7 and i < maxCount:    
        i += 1        
        
        version = packet[pos:pos+3]    
        pos += 3
        version = int(version,2)        
        versionSum += version
        pType = packet[pos:pos+3]
        pos += 3
        pType = int(pType,2)

        tPos += 6
        if pType == 4:        
            valStr = ''
            while True:
                # print(packet[pos])
                
                if packet[pos] == '1':
                    pos += 1
                    val = packet[pos:pos+4]
                    valStr += val
                    pos += 4                    
                    tPos += 5
                else:
                    pos += 1
                    val = packet[pos:pos+4]
                    valStr += val
                    val = int(valStr,2)
                    clist.append(val)
                    pos += 4
                    tPos += 5                  

                    break

        else:
                       
            lengthType = packet[pos]
            pos += 1
            lengthType = int(lengthType,2)
            tPos += 1
            tlist =[]
            if lengthType == 0:
                # next 15bit
                length = packet[pos : pos + 15]
                pos += 15
                length = int(length,2)
                parsePacket(packet[pos:pos+length],clist=tlist)
                pos += length

                tPos += 15 + length
            else:
                # next 11bit 
                count = packet[pos : pos + 11]
                pos += 11
                count = int(count,2)                
                
                tm = parsePacket(packet[pos:],count,tlist)
                pos += tm
                tPos += tm

            if pType ==0:                
                s = sum(tlist)                
                clist.append(s)
            elif pType ==1:
                s = reduce((lambda x, y: x * y), tlist)               
                clist.append(s)
            elif pType ==2:
                s = min(tlist)
                clist.append(s)
            elif pType ==3:
                s = max(tlist)
                clist.append(s)
            elif pType ==5:
                s = 0
                if len(tlist) != 2:
                    print(tlist)
                if tlist[0] > tlist[1]:
                    s = 1
                clist.append(s)
            elif pType ==6:
                s = 0
                if tlist[0] < tlist[1]:
                    s = 1
                clist.append(s)
            elif pType ==7:
                s = 0
                if tlist[0] == tlist[1]:
                    s = 1
                clist.append(s)
            
            
    
    return pos

ttt = []
parsePacket(data,clist=ttt)

print(versionSum)
print(ttt)