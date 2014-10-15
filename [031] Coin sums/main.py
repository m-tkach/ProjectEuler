SUM = 200
COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def go(i, s):
    if s == SUM:
        return 1
    if s > SUM:
        return 0

    res = 0
    for j, c in enumerate(COINS[i:]):
        res += go(j+i, s+c)
    return res


def calc():
    return go(0, 0)  
    

print(calc())
