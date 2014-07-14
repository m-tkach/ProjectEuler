N = 10000
d = [1] * N

def doo(x):
    q = 2
    while q * q < x:
        if x % q == 0:
            d[x] += q
            d[x] += x // q
        q += 1
    if q * q == x:
        d[x] += q

for x in range(N):
    doo(x)

ans = 0
for x in range(N):
    try:
        i = d[x]
        if d[i] == x and i != x:
            ans += x
    except IndexError:
        pass

print(ans)
    
