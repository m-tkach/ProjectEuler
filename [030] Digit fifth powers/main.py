MAX = 10**6


def is_digit_five_power_sum(x):
    s, n = 0, x
    while n > 0:
        d = n % 10
        n //= 10
        s += d * d * d * d * d
    return s == x


def calc():
    ans = 0
    for x in range(10, MAX):
        if is_digit_five_power_sum(x):
            ans += x
    return ans


print(calc())
    
