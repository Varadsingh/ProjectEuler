limit = 1000

sum3 = 0
i = 3
while i < limit:
    sum3 = sum3 + i
    i = i + 3

sum5 = 0
i = 5
while i < limit:
    sum5 = sum5 + i
    i = i + 5

sum15 = 0
i = 15
while i < limit:
    sum15 = sum15 + i
    i = i + 15

finalSum = sum3 + sum5 - sum15
print(finalSum)