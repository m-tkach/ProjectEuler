LEN = 1000
next = 0

a, b, i, l = 0, 1, 1, 0
while l < LEN:
    a, b = b, a + b
    i += 1
    if next <= 0:
        l = len(str(b))
        next = LEN - l
    next -= 1

print(i)
