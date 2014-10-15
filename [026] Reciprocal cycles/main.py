D = 1000

max_period = 0
answer = -1

for d in range(1, D):
    z = 1
    rem = []

    m = z % d
    while not m in rem:
        rem.append(m)
        z = m * 10
        m = z % d

    p = rem[::-1].index(m) + 1 if rem[-1] > 0 else 0
    if p > max_period:
        max_period = p
        answer = d

print(answer)
    
