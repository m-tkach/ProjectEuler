MAX_D = 10**6


primes = []
is_prime = []


def add_prime(x):
    primes.append(x)
    is_prime[x] = True


def gen_primes(n):
    for x in range(n):
        is_prime.append(False)
    
    add_prime(2)
    u = [False] * n
    for x in range(3, n, 2):
        if not u[x]:
            add_prime(x)
            u[x] = True
            for d in range(x*x, n, x):
                u[d] = True


def phi(n):
    result = n
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            result -= result // p
            while n % p == 0:
                n //= p
    if n > 1:
        result -= result // n
    return result


def calc():
    gen_primes(MAX_D+1)
    ans = 0
    for d in range(2, MAX_D+1):
        if is_prime[d]:
            ans += d - 1
        else:
            ans += phi(d)
    return ans


print(calc())


