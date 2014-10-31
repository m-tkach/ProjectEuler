PRIME_COUNT = 8
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


def to_list(i):
    if i == 0:
        return [0]
    ret = []
    while i > 0:
        ret.append(i % 10)
        i //= 10
    return ret[::-1]


def to_int(l):
    ans= 0
    for x in l:
        ans = ans * 10 + x
    return ans


def bit(val, index):
    return (val >> index) & 1


def calc():
    i, end = 0, DELTA
    while True:
        gen_primes(end)
        
        while i < len(primes):
            p = primes[i]
            p_list = to_list(p)
            L = len(p_list)
            MAX = 1 << L
            
            for mask in range(1, MAX):
                p_list = to_list(p)
                indexes = []
                for j in range(L):
                    if bit(mask, j):
                        indexes.append(j)

                for j in indexes:
                    if p_list[j] != p_list[indexes[0]]:
                        break
                else:
                    group = []
                    for d in range(10):
                        for j in indexes:
                            p_list[j] = d
                        if p_list[0] != 0:
                            new_p = to_int(p_list)
                            if is_prime(new_p):
                                group.append(new_p)
                    if len(group) == PRIME_COUNT:
                        group.sort()
                        return group
            i += 1
            
        end += DELTA
        
    return None


print(calc())
