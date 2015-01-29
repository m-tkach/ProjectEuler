"""
1234

134
234
123

234
134
123
"""


import itertools


def to_str(b):
    res = ''
    for x in b:
        res += str(x)
    return res


def solve(v):
    ds = [[], [], []]
    for i in range(3):
        for s in v:
            c = int(s[i])
            if not c in ds[i]:
                ds[i].append(c)

    best = [0] * 1000
    for p1 in itertools.permutations(ds[0]):
        for p2 in itertools.permutations(ds[1]):
            for p3 in itertools.permutations(ds[2]):
                a = []
                for x in p1:
                    a.append(x)
                for x in p2:
                    a.append(x)
                for x in p3:
                    a.append(x)
                used = [False] * len(a)
                u = 0
                for k in v:
                    j = 0
                    for c in k:
                        x = int(c)
                        while a[j] != x:
                            j += 1
                        if not used[j]:
                            used[j] = True
                            u += 1
                if u < len(best):
                    best = []
                    for i, x in enumerate(a):
                        if used[i]:
                            best.append(x)
    
    return to_str(best)


def calc():
    values = []
    with open('p079_keylog.txt', 'r') as ifs:
        for line in ifs:
            values.append(line.replace('\n', ''))
    return solve(values)


print(calc())
