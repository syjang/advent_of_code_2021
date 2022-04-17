from email.policy import default
import numpy as np 


with open('input.txt') as f:
    data = f.read().splitlines()
    algo = [int(x == "#") for x in data[0]]    
    image = np.array([[int(x == "#") for x in y] for y in data[2:]])



def enhance(img,test,curRow,curCol,fvalue):
    a = [-1,0,1]
    b = [-1,0,1]

    tmp = [0] * 9 

    for i, tr in enumerate(a):
        for j, tc in enumerate(b):
            r = curRow + tr
            c = curCol + tc
            if r < 0 or c < 0 or r >= maxRow or c >= maxCol:
                tmp[i*3 + j] = fvalue
                continue
            if img[r][c] == 1:
                tmp[i*3 + j] = 1
            else:
                tmp[i*3 + j] = 0


    s = ''.join(str(e) for e in tmp)
    idx = int(s,base=2)
    test[curRow][curCol] = algo[idx]   


    
fillvalue = 0
for i in range(50):    
    if fillvalue == 0:
        colTmp = np.zeros((1,image.shape[1]),dtype=np.int32)
    else:
        colTmp = np.ones((1,image.shape[1]),dtype=np.int32)

    image = np.concatenate((colTmp,image))
    image = np.concatenate((image,colTmp))

    if fillvalue == 0:
        tmp = np.zeros((image.shape[0],1),dtype=np.int32)
    else:
        tmp = np.ones((image.shape[0],1),dtype=np.int32)

    image = np.concatenate((image,tmp),axis=1)
    image = np.concatenate((tmp,image),axis=1)


    maxCol = image.shape[1]
    maxRow = image.shape[0]
    # print(image)

    copiedImg = image.copy()
    for i in range(maxRow):
        for j in range(maxCol):
            enhance(image,copiedImg,i,j,fillvalue)

    fillvalue = algo[0] if fillvalue == 0 else algo[-1]
    
    image = copiedImg
    # print(image.sum())

print(image.sum())

