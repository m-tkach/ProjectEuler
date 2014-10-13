N = 28124


def divs(n, div):
    div.append(1)
    d = 2
    while d * d < n:
        if n % d == 0:
            div.append(d)
            div.append(int(n / d))
        d += 1
    if d * d == n:
        div.append(d)
    div.sort()


def is_abundant(n):
    d = []
    divs(n, d)
    s = sum(d)
    return (s > n)


def bin_search(space, value):
    l, r = 0, len(space)
    while l + 1 < r:
        mid = int((l + r) / 2)
        if space[mid] > value:
            r = mid
        else:
            l = mid
    return (space[l] == value)
    

abundant = [x for x in range(1, N) if is_abundant(x)]

s = 0
for x in range(1, N):
    if x % 1000 == 0:
        print(x)
        
    ok = True
    for a in abundant:
        if a >= x:
            break
        if bin_search(abundant, x - a):
            ok = False
            break
    if ok:
        s += x

print(s)

    
