def febo(n):
    a = 1
    b = 2
    sum = 0
    while a < n:
        if a % 2 == 0:
            sum += a
        a, b = b , a+b
    print(sum)
febo(4000000)