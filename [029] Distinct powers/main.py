A = 100
B = 100


def calc():
    res = []
    for a in range(2, A + 1):
        for b in range(2, B + 1):
            res.append(a**b)

    res.sort()
    ans = 1
    i = 1
    while i < len(res):
        if res[i] != res[i - 1]:
            ans += 1
        i += 1
    return ans


print(calc())
        
