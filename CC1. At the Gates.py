def onesNtwos(n):
    global ones, twos
    while n > 0:
        ones = ones*10 + 1
        twos = twos*10 + 2
        n = n - 1

def revCoins(n):
    n = n + ones
    n = twos - n
    return(n)

def removeCoin(n):
    n = int(n/10)
    return(n)

ones = 0
twos = 0

numTestCases = int(input('PLEASE ENTER NUMBER OF TEST CASES: '))

while numTestCases > 0:
    tmp = str(input('PLEASE ENTER NUMBER OF COINS AND NUMBER OF REMOVALS ALLOWED: '))
    length = int(tmp.split()[0])
    onesNtwos(length)
    removal = int(tmp.split()[1])
    tmp = str(input('PLEASE PROVIDE THE COIN POSITIONS: '))
    num = 0
    for i in range(1,length+1):
        if tmp.split()[i-1] == 'H':
            num = num + (10**(length-i))
        if tmp.split()[i-1] == 'T':
            num = num
    tmp = num
    while removal > 0:
        if tmp%10 == 1:
            tmp = revCoins(tmp)
            tmp = removeCoin(tmp)
        else:
            tmp = removeCoin(tmp)
        removal = removal - 1
    hcount = 0        
    while int(tmp/10) > 0:
        if tmp%10 == 1:
            hcount = hcount + 1
        tmp = int(tmp/10)
    numTestCases = numTestCases - 1