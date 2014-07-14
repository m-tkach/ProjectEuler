N = 100

def fact(x):
    if x < 2:
        return x
    return x * fact(x-1)

ans = sum(int(c) for c in str(fact(N)))
print(ans)
