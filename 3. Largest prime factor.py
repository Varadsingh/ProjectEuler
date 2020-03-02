import math
#num = 13195
num = 600851475143

while num % 2 == 0:
    num = num / 2

prev = 0
for i in range(3,int(math.sqrt(num))+1,2):
    while num % i == 0:
        if i > prev:
            prev = i
        num = num / i

if prev == 0:
    prev = num
    
print(prev)