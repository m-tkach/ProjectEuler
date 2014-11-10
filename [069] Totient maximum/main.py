N = 10**6


def phi(x):
    res, d = x, 2
    while d * d <= x:
        if x % d == 0:
            res -= res // d
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        res -= res // x
    return res
        

def calc():
    best_n, best_phi = 0, 1
    for x in range(2, N+1):
        p = phi(x)
        if x * best_phi > best_n * p:
            best_n = x
            best_phi = p
    return best_n


print(calc())


"""
Fast solution:
answer = 1
for p in gen_primes(..):
    if answer * p > N:
        return answer
    answer *= p
"""
