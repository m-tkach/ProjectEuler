N = 100


def digit_sum(x):
    res = 0
    while x > 0:
        res += x % 10
        x //= 10
    return res


def calc():
    seq = [1, 2, 1]
    i = 1
    nom = [2, 3,]
    denom = [1, 1]
    while len(nom) < N:
        n = nom[-1] * seq[i] + nom[-2]
        d = denom[-1] * seq[i] + denom[-2]

        nom.append(n)
        denom.append(d)

        i += 1
        if i > 2:
            i = 0
            seq[1] += 2
    
    return digit_sum(nom[-1])


print(calc())
