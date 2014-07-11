N = 10001
p = [2,]
c = 3
while len(p) < N:
    prime = True
    for x in p:
        if x * x > c or not prime:
            break
        if c % x == 0:
            prime = False
    if prime:
        p.append(c)
    c += 2
print(p[-1])
