from math import sqrt


L = 1500000


def gcd(a, b):
    while a * b > 0:
        a, b = b, a % b
    return a + b


def calc():
    cache = [0] * (L+1)

    n = int(sqrt(L)) + 1
    for x in range(1, n):
        for y in range(x+1, n, 2):
            if gcd(x, y) != 1:
                continue
            a = 2 * x * y
            b = y * y - x * x
            c = y * y + x * x
            s = a + b + c
            
            k = 1
            while s <= L:
                cache[s] += 1
                k += 1
                s = k * a + k * b + k * c
   
    return sum(x for x in cache if x == 1)


print(calc())
