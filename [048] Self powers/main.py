MOD = int(10**10)
MAX = 1000


def power(x, p):
    res = 1
    while p > 0:
        if p % 2 == 1:
            res *= x
            res %= MOD
        x *= x
        x %= MOD
        p //= 2
    return res


def calc():
    ans = 0
    for x in range(1, MAX+1):
        ans += power(x, x)
        ans %= MOD
    return ans
        
           
print(calc())
