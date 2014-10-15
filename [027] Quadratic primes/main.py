A = 1000
B = 1000


prime = [2, 3, ]


def gen_prime(n):
    if n <= prime[-1]:
        return
    s = prime[-1] + 2
    for x in range(s, n + 1, 2):
        ok = True
        for p in prime:
            if p * p > x:
                break
            if x % p == 0:
                ok = False
                break
        if ok:
            prime.append(x)


def binary_search(space, x):
    l, r = 0, len(space)
    while l + 1 < r:
        mid = (l + r) // 2
        if space[mid] > x:
            r = mid
        else:
            l = mid
    return (space[l] == x)


def is_prime(n):
    gen_prime(n)
    return binary_search(prime, n)


def calc():
    ans = 0
    n_max = 0
    for a in range(1 - A, A):
        for b in range(1 - B, B):
            n = 0
            while is_prime(n * n + a * n + b):
                n += 1
            if n > n_max:
                n_max = n
                ans = a * b
    return ans


print(calc())
            

            
    
