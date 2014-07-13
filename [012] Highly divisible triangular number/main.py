def divs_count(x):
    count = 0
    d = 1
    while d * d < x:
        if x % d == 0:
            count += 2
        d += 1
    if d * d == x:
        count += 1
    return count

M = 500
z = 0
x = 1
while divs_count(z) <= M:
    z += x
    x += 1
print(z)
