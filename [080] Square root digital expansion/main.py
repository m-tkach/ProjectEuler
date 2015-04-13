MAX = 100
LEN = 100
BASE = 25


def check(x, int_part, dec_part):
    cur = [d for d in dec_part[::-1]]
    cur.append(int_part)
    res = []
    for i, a in enumerate(cur):
        for j, b in enumerate(cur):
            k = i + j
            while len(res) <= k:
                res.append(0)
            res[k] += a * b
        for k, c in enumerate(res[:-1]):
            if res[k] >= 10**BASE:
                res[k + 1] += res[k] // 10**BASE
                res[k] %= 10**BASE
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    if res[-1] < x:
        return True
    elif res[-1] > x:
        return False
    return sum(res[:-1]) == 0
            
    

def sum_of_decimal_digits_in_root(x):
    int_part = 0
    while int_part * int_part <= x:
        int_part += 1
    int_part -= 1

    decimal = [0] * (LEN // BASE)
    for i in range(len(decimal)):
        l, r = 0, 10**BASE
        while l + 1 < r:
            d = (r + l) // 2
            decimal[i] = int(d)
            if check(x, int_part, decimal):
                l = d
            else:
                r = d
        decimal[i] = l

    res = [int(d) for d in str(int_part)]
    for d in decimal:
        res.extend([int(c) for c in str(d).rjust(BASE, '0')])

    return sum(res[:LEN])


def calc():
    not_irr = set()
    for x in range(1, int(MAX**0.5) + 1):
        not_irr.add(x * x)

    res = 0
    for x in range(1, MAX):
        if x not in not_irr:
            res += sum_of_decimal_digits_in_root(x)
    return res
    

print(calc())
