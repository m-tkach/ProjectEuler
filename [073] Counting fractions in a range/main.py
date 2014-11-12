MAX_D = 12000
LEFT = (1, 3)
RIGHT = (1, 2)


def calc():
    ans = 0
    borders = [(LEFT, RIGHT)]
    while len(borders) > 0:
        border = borders.pop()
        n1, d1 = border[0]
        n2, d2 = border[1]
        n, d = n1 + n2, d1 + d2
        if d <= MAX_D:
            ans += 1
            borders.append(((n1, d1), (n, d)))
            borders.append(((n, d), (n2, d2)))
    return ans


print(calc())


