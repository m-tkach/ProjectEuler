MAX_D = 10**6
N, D = 3, 7


def calc():
    left_n, left_d = 2, 5
    i = (MAX_D - left_d) // D
    left_n += i * N
    return left_n


print(calc())


