a, b, res = 0, 2, 0
while b <= 4000000:
    res += b
    a, b = b, 4 * b + a
print(res)
