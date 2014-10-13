LEN = 1000
next = 0

a, b, i = 0, 1, 1
while True:
    a, b = b, a + b
    i += 1
    if next <= 0:
        l = len(str(b))
        if l >= LEN:
            break
        next = LEN - l
    next -= 1

print(i)
