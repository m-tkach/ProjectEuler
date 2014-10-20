def has_uni_digits(x):
    d = []
    while x > 0:
        z = x % 10
        if z in d:
            return False
        d.append(z)
        x //= 10
    return True


def is_pandigital(s):
    if len(s) != 9:
        return False
    p = ''.join(sorted(s))
    return p == '123456789'


def calc():
    best = 0
    for x in range(1, 10000):
        if has_uni_digits(x):
            s = ''
            n = 1
            while len(s) < 9:
                p = x * n
                s += str(p)
                n += 1
            if is_pandigital(s):
                i = int(s)
                if i > best:
                    best = i
    return best
                

print(calc())
