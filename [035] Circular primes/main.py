N = 1000000


def search(space, v):
    l, r = 0, len(space)
    while l + 1 < r:
        mid = (l + r) // 2
        if space[mid] > v:
            r = mid
        else:
            l = mid
    return l if space[l] == v else -1


def has_even_digit(x):
    n = x
    while n > 0:
        d = n % 10
        if d % 2 == 0:
            return True
        n //= 10
    return False


def get_uid(x):
    if x % 2 == 0:
        return 0
    return x // 2


def next(x):
    n = x
    d = n % 10
    n //= 10
    if n == 0:
        return d
    return n + d * 10**len(str(n))


def gen_primes():
    p = [2, ]
    u = [False] * (N // 2)
    
    for x in range(3, N, 2):
        i = get_uid(x)
        if not u[i]:
            u[i] = True
            for a in range(x * x, N, x):
                i = get_uid(a)
                u[i] = True
                
            if not has_even_digit(x):
                p.append(x)
    
    return p


def calc():
    ans = 0
    primes = gen_primes()
    used = [False] * len(primes)
    
    for i, p in enumerate(primes):
        if used[i]:
            continue
        
        used[i] = True        
        cnt = 1
        ok = True
        
        x = next(p)
        while x != p:
            j = search(primes, x)
            if j == -1:
                ok = False
            else:
                used[j] = True
                cnt += 1
            x = next(x)

        if ok:
            ans += cnt
            
    return ans


print(calc())

    
