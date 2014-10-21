primes = []
def gen_primes():
    primes.append(2)
    for x in range(3, 100, 2):
        for p in primes:
            if p * p > x:
                primes.append(x)
                break
            if x % p == 0:
                break


def is_eq_digits(a, b):
    d = [0] * 10
    while a > 0:
        d[a % 10] += 1
        a //= 10
    while b > 0:
        d[b % 10] -= 1
        b //= 10
    for q in d:
        if q != 0:
            return False
    return True


def search(space, v):
    l, r = 0, len(space)
    while l + 1 < r:
        m = (l + r) // 2
        if space[m] > v:
            r = m
        else:
            l = m
    return space[l] == v


def calc():
    gen_primes()
    
    primes_4 = []
    for x in range(1001, 10000, 2):
        for p in primes:
            if x % p == 0:
                break
        else:
            primes_4.append(x)

    ans = 0
    for i, p in enumerate(primes_4):
        for q in primes_4[i+1:]:
            if is_eq_digits(p, q):
                diff = q - p
                t = q + diff
                if t > 9999:
                    break
                if is_eq_digits(q, t) and search(primes_4, t):
                    ans = p * 10**8 + q * 10**4 + t
    return ans

          
print(calc())
