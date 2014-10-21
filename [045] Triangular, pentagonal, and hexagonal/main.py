def triangular(x):
    return x * (x + 1) // 2


def pentagonal(x):
    return x * (3 * x - 1) // 2


def hexagonal(x):
    return x * (2 * x - 1)


def is_triangular(x):
    l, r = 0, x+1
    while l + 1 < r:
        m = (l + r) // 2
        if triangular(m) > x:
            r = m
        else:
            l = m  
    return triangular(l) == x


def is_pentagonal(x):
    l, r = 0, x+1
    while l + 1 < r:
        m = (l + r) // 2
        if pentagonal(m) > x:
            r = m
        else:
            l = m  
    return pentagonal(l) == x


def calc():
    i = 144
    while True:
        h = hexagonal(i)
        if is_pentagonal(h) and is_triangular(h):
            return h
        i += 1
    return None

           
print(calc())
