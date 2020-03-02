match = 0
matchNum = []
def revNum(n):
    tmp = ''
    tmpNum = n
    
    while int(tmpNum/10) > 0:
        digit = tmpNum%10
        tmp = tmp + str(digit)
        tmpNum = int(tmpNum/10)
    tmp = tmp + str(tmpNum%10)
    
    if (tmp == str(n)):
        return(1)
    else:
        return(0)

i = 999
while i >= 100:
    j = 999
    while j >= i:
        match = revNum(i*j)
        if match == 1:
            matchNum.append(i*j)
        j = j - 1
    if match == 1:
        break
    i = i - 1

print(max(matchNum))