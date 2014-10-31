MAX_MULTIPLIER = 6


def to_int(l):
    ans = 0
    for x in l:
        ans = ans * 10 + x
    return ans


def to_sort_list(i):
    if i == 0:
        return [0]
    ret = []
    while i > 0:
        ret.append(i % 10)
        i //= 10
    ret.sort()
    return ret


def next(v):
    v += 1
    max_multi_v = v * MAX_MULTIPLIER
    len_v = len(str(v))
    if len_v != len(str(max_multi_v)):
        v = int('1' + ('0' * len_v))
    return v


def check(val):
    checked = to_int(to_sort_list(val))
    for multiplier in range(2, MAX_MULTIPLIER+1):
        x = val * multiplier
        if checked != to_int(to_sort_list(x)):
            return False
    return True


def calc():
    i = 10
    while True:
        if (check(i)):
            return i
        i = next(i)
    return None


print(calc())
