N = 10**7


primes = []
def gen_primes(n):
    primes.append(2)
    u = [False] * (n // 2)
    for x in range(3, n, 2):
        i = x // 2
        if not u[i]:
            primes.append(x)
            u[i] = True
            for d in range(x*x, n, x):
                j = d // 2 if d % 2 == 1 else 0
                u[j] = True


def lower_bound(space, x):
    l, r = 0, len(space)
    while l + 1 < r:
        mid = (l + r) // 2
        if space[mid] > x:
            r = mid
        else:
            l = mid
    return l
                

def to_sorted_list(x):
    if x == 0:
        return [0]
    res = []
    while x > 0:
        res.append(x % 10)
        x //= 10
    res.sort()
    return res


def is_eq_perm(a, b):
    x = to_sorted_list(a)
    y = to_sorted_list(b)
    if len(x) != len(y):
        return False
    for i, j in zip(x, y):
        if i != j:
            return False
    return True


def calc():
    gen_primes(N)
    best_n, best_phi = 1000000, 1
    for i, p in enumerate(primes):
        if p * p >= N:
            break
        j = lower_bound(primes, N // p)
        for q in primes[j::-1]:
            n = p * q
            ph = (p-1) * (q-1)
            if is_eq_perm(n, ph):
                if n * best_phi < best_n * ph:
                    best_n = n
                    best_phi = ph
                    break
    return best_n


print(calc())

