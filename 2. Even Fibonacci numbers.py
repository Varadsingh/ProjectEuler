limit = 4000000

fib = 1
prevfib = 0
sumeven = 0
while fib <= limit:
    tmp = fib
    fib = fib + prevfib
    prevfib = tmp
    if fib%2 == 0:
        sumeven = sumeven + fib

print(sumeven)