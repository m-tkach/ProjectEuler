SIZE = 5


def get_digits_count(v):
    ans = [0] * 10
    if v == 0:
        ans[0] = 1
        return ans

    while v > 0:
        d = v % 10
        ans[d] += 1
        v //= 10
    return ans


def to_comparison_string(v):
    hg = get_digits_count(v)
    s = ""
    for c in hg:
        s += str(c) + '_'
    return s


def calc():
    histogram = dict()
    min_cubic = dict()
    x = 1
    while True:
        cubic = x * x * x
        stroke = to_comparison_string(cubic)

        if stroke in histogram:
            histogram[stroke] += 1
        else:
            min_cubic[stroke] = cubic
            histogram[stroke] = 1

        if histogram[stroke] >= SIZE:
            return min_cubic[stroke]

        x += 1
    
    return None


print(calc())
