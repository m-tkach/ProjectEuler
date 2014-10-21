MAX = 4000


def get_pentagon(x):
    return x * (3 * x - 1)


def is_pentagon(x):
    l, r = 0, MAX
    while l + 1 < r:
        m = (l + r) // 2
        if get_pentagon(m) > x:
            r = m
        else:
            l = m
    return x == get_pentagon(l)


def calc():
    ans = -1
    for k in range(1, MAX):
        for j in range(1, k):
            d = get_pentagon(k) - get_pentagon(j)
            s = get_pentagon(k) + get_pentagon(j)
            if is_pentagon(d) and is_pentagon(s):
                if ans == -1 or ans > d:
                    ans = d
    return ans // 2

           
print(calc())
