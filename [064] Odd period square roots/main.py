from math import sqrt


N = 10000


def find_period_len(x):
    coef = dict()
    a, n, d, i = int(sqrt(x)), 0, 1, 1
    while not (a, n, d) in coef:        
        coef[(a, n, d)] = i
        i += 1

        n = d * a - n
        d = (x - n * n) // d
        if d == 0:
            return 0
        a = (int(sqrt(x)) + n) // d
    
    return i - coef[(a, n, d)]


def check_period(period):
    if period % 2 == 0:
        return False
    return True


def calc():
    ans = 0
    for x in range(1, N+1):
        period_len = find_period_len(x)
        if check_period(period_len):
            ans += 1
    return ans


print(calc())
