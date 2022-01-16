import copy

class board:
    def __init__(self):
        self.data = [0] * 5

    def bingo(self, cmd):
        tmp = copy.deepcopy(self.data)
        for idx,c in enumerate(cmd):
            for i in range(5):
                for j in range(5):
                    if tmp[i][j] == c:
                        tmp[i][j] = '-1'
                        break

            f = False

            for i in range(5):
                ct = 0
                ct2 = 0
                for j in range(5):
                    if tmp[i][j] == '-1':
                        ct +=1
                    if tmp[j][i] == '-1':
                        ct2 +=1
                
                if ct == 5 or ct2 == 5:
                    f = True
                    break
            
            if f:
                self.maxcmd = idx
                self.c = c 
                break
        
        s = 0 
        for i in range(5):
            for j in range(5):
                if int(tmp[i][j]) == -1 :
                    continue
                s += int(tmp[i][j])
        
        self.ret = s * int(cmd[idx])
        self.ret2= s * int(c)


cmd = None
boards = []
with open('input.txt') as f:
    l = f.readlines()
    cmd = l[0]
    cmd = cmd.split(',')
    l = l[2:]
    bd = board()
    r = 0
    for i,s in enumerate(l):
        if s == '\n':
            boards.append(bd)
            bd = board()            
            r = 0
            continue
        s = s.replace('\n','')
        sp = s.split(' ')
        bd.data[r] = [ele for ele in sp if ele != '']
        r += 1 

    boards.append(bd)

    for b in boards:
        b.bingo(cmd)

    m = 999999999
    retIdx = 9999999

    m2 = -1
    retIdx2 = 0
    for idx, b in enumerate(boards):
        if m > b.maxcmd:
            retIdx = idx
            m = b.maxcmd
        if m2 < b.maxcmd:
            retIdx2 = idx
            m2 = b.maxcmd

    #anw
    print(boards[retIdx].ret)

    print(boards[retIdx2].ret)
