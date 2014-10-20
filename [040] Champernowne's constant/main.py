I = [int(10**p) for p in range(0, 7)]

def naive():
    d = [0, ]
    x = 1
    while len(d) <= I[-1]:
        s = str(x)
        for c in s:
            d.append(int(c))
        x += 1
    ans = 1
    for i in I:
        ans *= d[i]
    return ans

print(naive())
