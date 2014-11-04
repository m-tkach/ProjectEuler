LIMIT = 0.1


primes = [2, 3,]
def gen_primes(n):
    if primes[-1] >= n:
        return
    for x in range(primes[-1]+2, n+1, 2):
        for p in primes:
            if p * p > x:
                primes.append(x)
                break
            if x % p == 0:
                break


def is_prime(x):
    gen_primes(int(x**0.5) + 1)
    for p in primes:
        if p * p > x:
            return 1
        if x % p == 0:
            return 0
    return 1


def calc():
    gen_primes(10**5)
    
    start, length = 1, 1
    total, prime = 1, 0
    while prime >= total * LIMIT or prime == 0:
        length += 2
        diag = [start + i * (length - 1) for i in range(1, 4)]
        
        total += 4
        prime += sum([is_prime(d) for d in diag])
        
        start = length * length

    return length
        

print(calc())
