def sqr(n):
    return(n*n)

i = 1
sumOfSqr = 0
sumOfNum = 0
while i <= 100:
    sumOfSqr = sumOfSqr + sqr(i)
    sumOfNum = sumOfNum + i
    i = i + 1

print(sqr(sumOfNum) - sumOfSqr)