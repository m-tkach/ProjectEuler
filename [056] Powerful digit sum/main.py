A, B = 100, 100


def pow(x, p):
    res = 1
    while p > 0:
        if p & 1:
            res *= x
        x *= x
        p //= 2
    return res


def digit_sum(x):
    ans = 0
    while x > 0:
        ans += x % 10
        x //= 10
    return ans


def calc():
    ans = 0
    for a in range(A):
        for b in range(B):
            temp = digit_sum(pow(a, b))
            if temp > ans:
                ans = temp
    return ans
 

print(calc())
