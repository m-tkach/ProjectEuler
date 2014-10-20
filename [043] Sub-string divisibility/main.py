divs = [1, 2, 3, 5, 7, 11, 13, 17]


def has_uni_digits(x, size):
    d = [0] * 10
    for s in range(size):
        z = x % 10
        if d[z] != 0:
            return False
        d[z] += 1
        x //= 10
    return True


def go(x, size):
    if not has_uni_digits(x, size):
        return 0
    if size == 10:
        return x
    
    d = []
    n = x
    for i in range(size):
        d.append(n % 10)
        n //= 10

    ans = 0
    for a in range(10):
        if a in d:
            continue
        n = a * 10**size + x
        
        i = 1 - size
        sub = n // 10**(size-2)
        
        if sub % divs[i] == 0:
            ans += go(n, size+1)
    
    return ans


def calc():
    return sum([go(x, 3) for x in range(divs[-1], 1000, divs[-1])])
                

print(calc())
