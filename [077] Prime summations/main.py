LIMIT = 5000


p = [2, 3,]
def gen_primes(length):
    x = p[-1] + 2
    while len(p) <= length:
        for d in p:
            if d * d > x:
                p.append(x)
                break
            if x % d == 0:
                break
        x += 2


def prime(i):
    gen_primes(i)
    return p[i]


def go(x, s, n, dp):
    if s > n:
        return 0
    if s == n:
        return 1
    
    if (x, s) in dp:
        return dp[(x, s)]
    
    res = 0
    z = x
    while s + prime(z) <= n:
        res += go(z, s+prime(z), n, dp)
        z += 1

    dp[(x, s)] = res
    return res


def calc():
    n = 2
    while True:
        ans = go(0, 0, n, dict())
        if n in p:
            ans -= 1
        if ans > LIMIT:
            return n
        n += 1
    return None


print(calc())
