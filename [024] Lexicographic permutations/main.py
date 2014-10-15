L = 10
N = 1000000


def fact(n):
    f = [1, ]
    for x in range(1, n + 1):
        f.append(f[-1] * x)
    return f


def perm(space, n):
    p = []
    
    space.sort()
    f = fact(len(space))
    used = [False] * L

    size = L - 1
    n -= 1
    while size >= 0:
        i = n // f[size]
        n %= f[size]
        
        k = -1
        for e, x in enumerate(space):
            if not used[e]:
                k += 1
                if k == i:
                    p.append(x)
                    used[e] = True
                    break
        
        size -= 1

    return p


a = [x for x in range(L)]
p = perm(a, N)
print(''.join(map(str, p)))

