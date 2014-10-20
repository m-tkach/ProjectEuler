from itertools import permutations


primes = []
def gen_primes(n):
    used = [False] * (n // 2)
    primes.append(2)
    for x in range(3, n, 2):
        i = x // 2
        if not used[i]:
            primes.append(x)
            used[i] = True
            for d in range(x*x, n, x):
                j = d // 2 if d % 2 == 1 else 0
                used[j] = True
            


def is_pandigital(x):
    s = ''.join(sorted(str(x)))
    return s == '123456789'[:len(s)]


def is_prime(x):
    last = x % 10
    if last == 5 or last % 2 == 0:
        return False
    for p in primes:
        if p * p > x:
            return True
        if x % p == 0:
            return False
    return True


def to_int(array):
    return int(''.join(map(str, array)))


def calc():
    len_sum = 0
    lens = []
    for l in range(1, 10):
        len_sum += l
        if len_sum % 3 != 0:
            lens.append(l)

    gen_primes(int((10**lens[-1])**0.5) + 1)
    
    for mx in lens[::-1]:
        d = [x for x in range(mx, 0, -1)]
        for p in permutations(d):
            i = to_int(p)
            if is_prime(i) and is_pandigital(i):
                return i
    return None
                

print(calc())
