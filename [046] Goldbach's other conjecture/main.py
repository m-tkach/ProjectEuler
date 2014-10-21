primes = [2, 3,]
def gen_primes(n):
    if primes[-1] >= n:
        return
    for x in range(primes[-1], n+1, 2):
        for p in primes:
            if p * p > x:
                primes.append(x)
                break
            if x % p == 0:
                break


def is_prime(x):
    gen_primes(x)
    l, r = 0, len(primes)
    while l + 1 < r:
        m = (l + r) // 2
        if primes[m] > x:
            r = m
        else:
            l = m
    return primes[l] == x
            


def calc():
    v = 9
    while True:
        if not is_prime(v):
            for s in range(1, int((v*0.5)**0.5+1)):
                x = v - 2 * s * s
                if is_prime(x):
                    break
            else:
                return v
        v += 2
    return None

           
print(calc())
