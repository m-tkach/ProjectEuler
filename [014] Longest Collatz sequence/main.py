N = 10**6

def foo(x):
    iter = 1
    while x > 1:
        if x % 2:
            x = 3 * x + 1
        else:
            x = x // 2
        iter += 1
    return iter

c = 0
res = 0
for x in range(N):
    f = foo(x)
    if f > c:
        c = f
        res = x
print(res)
