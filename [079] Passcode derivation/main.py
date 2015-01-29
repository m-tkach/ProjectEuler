"""
1234

134
234
123

234
134
123
"""


def solve(v):
    ans = 100
    while True:
        if ans % 100000 == 0:
            print(ans)
        ok = True
        for s in v:
            k = 0
            for c in str(ans):
                if k == 3:
                    break
                if s[k] == c:
                    k += 1
            if k < 3:
                ok = False
                break
        if ok:
            break
        ans += 1
    return ans


def calc():
    values = []
    with open('p079_keylog.txt', 'r') as ifs:
        for line in ifs:
            values.append(line)
    return solve(values)


print(calc())
