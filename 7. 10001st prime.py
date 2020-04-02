# 10001st prime
def chkPrmCnt(n):
    global myLst
    myLst = [1]*(n+1)
    myLst[0]=0
    myLst[1]=0
    for i in range(2,n):
        if i*i <= n:
            j = i*i
            while j <= n:
                myLst[j] = 0
                j = j + i
    return(sum(myLst))
st = 0
en = 100
prmCntr = chkPrmCnt(en)
n = 10001
while prmCntr != n:
    prmCntr = chkPrmCnt(en)
    if prmCntr < n:
        st = en
        en = en + en//2
    if prmCntr > n:
        mySum = 0
        for i in range(2,en):
            mySum = mySum + myLst[i]
            if mySum == n:
                print(i)
                prmCntr = n
                break