
from struct import pack


def convertHexToBin(value : str) -> str:
    return bin(int(value,16))[2:].zfill(4)



with open('input.txt') as f:
    temp = f.read()
    oridata = [convertHexToBin(s) for s in temp]    
    data = ''
    for s in oridata:
        data += s


clist = []

versionSum = 0
def parsePacket(packet : list ,maxCount:int = 100000000):    
    global versionSum
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


        if pType == 4:        
            while True:
                # print(packet[pos])
                if packet[pos] == '1':
                    pos += 1
                    val = packet[pos:pos+4]
                    val = int(val,2)
                    clist.append(val)
                    pos += 4
                else:
                    pos += 1
                    val = packet[pos:pos+4]
                    val = int(val,2)
                    clist.append(val)
                    pos += 4
                    break

        else:
            tmp =''
            if pType ==0:
                tmp = '+'
            elif pType ==1:
                tmp = '*'
            elif pType ==2:
                tmp = 'min'
            elif pType ==3:
                tmp = 'max'
            elif pType ==5:
                tmp = '>'
            elif pType ==6:
                tmp = '<'
            elif pType ==7:
                tmp = '='
            
            clist.append('(')
            clist.append(tmp)
            
            lengthType = packet[pos]
            pos += 1
            lengthType = int(lengthType,2)

            if lengthType == 0:
                # next 15bit
                length = packet[pos : pos + 15]
                pos += 15
                length = int(length,2)
                parsePacket(packet[pos:pos+length])
                pos += length
            else:
                # next 11bit 
                count = packet[pos : pos + 11]
                pos += 11
                count = int(count,2)                
                pos += parsePacket(packet[pos:],count)
            
            clist.append(')')
    
    return pos


parsePacket(data)

print(versionSum)
print(clist)        
        




    

