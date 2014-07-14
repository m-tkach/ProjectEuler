dm = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
D, M, Y = 2, 1, 1901
res = 0


def is_leap(year):
    return year % 4 == 0


while Y < 2001:
    
    D += dm[M] % 7
    if D == 7:
        res += 1
    while D > 7:
        D -= 7

    M += 1
    while M > 12:
        M -= 12
        Y += 1
        if is_leap(Y):
            dm[2] = 29
        else:
            dm[2] = 28


print(res)

