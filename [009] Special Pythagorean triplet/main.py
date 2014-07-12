N = 1000
for a in range(N):
    for b in range(a+1, N):
        c = (a**2 + b**2)**0.5
        if a < b < c and a + b + c == N:
            print(int(a * b * c))
