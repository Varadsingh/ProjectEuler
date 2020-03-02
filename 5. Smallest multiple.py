def iniLst(n):
    i = 1
    tmp = []
    while i <= n:
        tmp.append(0)
        i = i + 1
    return(tmp.copy())
    
def primFactor(n):
    tmpp=iniLst(21)
    i = 2
    tmp = n
    while tmp > 1:
        if tmp % i == 0:
            tmpp[i] = tmpp[i] + 1
            tmp = int(tmp/i)
        else:
            i = i + 1
        if p[i] < tmpp[i]:
            p[i] = tmpp[i]

p = iniLst(21)
i = 1
while i <= 20:
    primFactor(i)
    i = i + 1
    
prod = 1
for i in range(1,21):
    while p[i] > 0:
        prod = prod * i
        p[i] = p[i] - 1
    i = i + 1