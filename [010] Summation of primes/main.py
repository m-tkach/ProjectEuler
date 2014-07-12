M = 2 * 10**6
u = [1] * M
u[0], u[1] = 0, 0
for i, x in enumerate(u):
    if x:
        j = i * i
        while j < M:
            u[j] = 0
            j += i
res = sum([x * i for i, x in enumerate(u)])
print(res)
    
    
