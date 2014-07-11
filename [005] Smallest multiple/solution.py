def gcd(x, y):
    while (x * y != 0):
        x, y = y, x % y
    return x + y

def lcm(x, y):
    return x // gcd(x, y) * y

res = 1
for x in range(1, 21):
    res = lcm(res, x)
print(res)
