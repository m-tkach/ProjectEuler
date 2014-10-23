PRIME_COUNT = 7
DELTA = 10000


primes = [2, 3, ]
def gen_primes(n):
    if n <= primes[-1]:
        return
    for x in range(primes[-1]+2, n, 2):
        for p in primes:
            if p * p > x:
                primes.append(x)
                break
            if x % p == 0:
                break


def is_prime(x):
    gen_primes(x+1)
    l, r = 0, len(primes)
    while l + 1 < r:
        m = (l + r) // 2
        if primes[m] > x:
            r = m
        else:
            l = m
    return primes[l] == x


def update_number(x, pos, digit):
    # positions: ...43210
    ten = 10**pos
    v = x + digit * ten - (x % (ten * 10) - x % ten)
    return v


def calc():
    i, end = 0, DELTA
    while True:
        gen_primes(end)
        
        while i < len(primes):
            p = primes[i]
            size = len(str(p))
            for pos in range(size):
                prime_list = []
                start = 0 if pos + 1 < size else 1
                for d in range(start, 10):
                    v = update_number(p, pos, d)
                    if is_prime(v):
                        prime_list.append(v)
                if len(prime_list) == PRIME_COUNT:
                    return prime_list
                if p == 56003:
                    print(prime_list)
            i += 1
        
        end += DELTA
    pass


print(calc())
