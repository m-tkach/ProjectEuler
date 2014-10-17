N = 10**6
primes = [2, ]


def has_even_digit_except_first_2(x):
    n = x
    while n > 9:
        if n % 2 == 0:
            return True
        n //= 10
    return n % 2 == 0 and n != 2


def init_primes():
    u = [False] * (N // 2)
    for x in range(3, N, 2):
        i = x // 2
        if not u[i]:
            u[i] = True
            for d in range(x*x, N, x):
                j = d // 2 if d % 2 == 1 else 0
                u[j] = True
            primes.append(x)


def gen_primes(n):
    if primes[-1] >= n:
        return
    if primes[-1] == 2:
        primes.append(3)
    for x in range(primes[-1]+2, n+1, 2):
        ok = True
        for p in primes:
            if p * p > x:
                break
            if x % p == 0:
                ok = False
                break
        if ok:
            primes.append(x)


def search(space, v):
    l, r = 0, len(space)
    while l + 1 < r:
        mid = (l + r) // 2
        if space[mid] > v:
            r = mid
        else:
            l = mid
    return space[l] == v


def is_prime(x):
    gen_primes(x)
    return search(primes, x)


def only_primes(x):
    n = x
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True


def check_left_to_right(x):
    n = x
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True


def check_right_to_left(x):
    n = x
    p = N
    while p > 1:
        n %= p
        if not is_prime(n):
            return False
        p //= 10

    return True


def check(z):
    return check_left_to_right(z) and check_right_to_left(z)

    
def calc():
    res = 0
    init_primes()
    for p in primes[4:]:
        if has_even_digit_except_first_2(p):
            continue
        if check(p):
            res += p
    return res


print(calc())
