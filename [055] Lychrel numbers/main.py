MAX = 10000
ITER = 50


def to_list(v):
    if v == 0:
        return [0]
    ret = []
    while v > 0:
        ret.append(v % 10)
        v //= 10
    return ret[::-1]


def to_int(l):
    ans = 0
    for x in l:
        ans = ans * 10 + x
    return ans


def is_palindrome(x):
    p = to_list(x)
    l, r, = 0, len(p)-1
    while l < r:
        if p[l] != p[r]:
            return False
        l += 1
        r -= 1
    return True


def reverse(x):
    return to_int(to_list(x)[::-1])


def is_lychrel(x):
    it = 1
    while it <= ITER:
        x += reverse(x)
        if is_palindrome(x):
            return False
        it += 1
    return True


def calc():
    ans = 0
    for x in range(1, MAX):
        if is_lychrel(x):
            ans += 1
    return ans
        

print(calc())
