from math import sqrt


D = 1000


def is_sq(x):
    sqrt_x = int(sqrt(x))
    return sqrt_x * sqrt_x == x


def force(d):
    a, n, x = int(sqrt(d)), 0, 1
    f = [(1, 0), (a, 1)]
    while f[-1][0]**2 - d * f[-1][1]**2 != 1.0:
        n = x * a - n
        x = (d - n * n) // x
        a = (int(sqrt(d)) + n) // x

        nom = a * f[-1][0] + f[-2][0]
        denom = a * f[-1][1] + f[-2][1]

        f.append((nom, denom))
        
    return f[-1][0]
    

def calc():
    max_x, ans = -1, -1
    for d in range(1, D+1):
        if not is_sq(d):
            x = force(d)
            if x > max_x:
                max_x = x
                ans = d
    return ans


print(calc())
