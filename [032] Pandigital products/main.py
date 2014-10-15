def product_str(a, b):
    x, y, z = str(a), str(b), str(a * b)
    return x + y + z


def is_pandigital(s):
    if len(s) != 9:
        return False
    s = ''.join(sorted(s))
    return s == '123456789'


def calc():
    res = set()
    for x in range(1, 100):
        for y in range(100, 10000):
            s = product_str(x, y)
            if (len(s) > 9):
                break
            if is_pandigital(s):
                res.add(x * y)
    return sum(res)


print(calc())
    
    
    
    
