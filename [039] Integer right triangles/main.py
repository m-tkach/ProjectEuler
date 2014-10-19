N = 1000
SQ = [x*x for x in range(N+1)]


def get_int_square(x):
    l, r = 0, len(SQ)
    while l + 1 < r:
        mid = (l + r) // 2
        if SQ[mid] > x:
            r = mid
        else:
            l = mid
    return l if SQ[l] == x else -1


def calc():
    cnt = [0] * (N+1)
    for a in range(1, 251):
        for b in range(a, 501):
            c = get_int_square(a * a + b * b)
            if c != -1:
                p = a + b + c
                if p <= N:
                    cnt[p] += 1
    max_p = 0
    for p in range(1, N+1):
        if cnt[p] > cnt[max_p]:
            max_p = p
    return max_p
                

print(calc())
