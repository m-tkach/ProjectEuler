MAX = 10**6
primes = []
is_p = [False] * MAX


def gen_primes():
    primes.append(2)
    u = [False] * (MAX // 2)
    for x in range(3, MAX, 2):
        i = x // 2
        if not u[i]:
            primes.append(x)
            u[i] = True
            for d in range(x*x, MAX, x):
                j = (d // 2) * (d % 2)
                u[j] = True

    for p in primes:
        is_p[p] = True


def is_prime(x):
    if x < 0 or x >= primes[-1]:
        return False
    return is_p[x]


def calc():
    gen_primes()

    s = [primes[0], ]
    for p in primes[1:]:
        s.append(p + s[-1])

    best, max_len = primes[0], 1
    for l in range(0, len(s)):
        for r in range(l+max_len, len(s)):
            z = s[r] - (s[l-1] if l != 0 else 0)
            if z > MAX:
                break
            if is_prime(z) and r - l + 1 > max_len:
                max_len = r - l + 1
                best = z
    
    return best


print(calc())
