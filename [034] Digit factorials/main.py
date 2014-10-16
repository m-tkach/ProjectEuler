def calc():
    fact = [1, ]
    for x in range(1, 10):
        fact.append(fact[-1] * x)

    ans = 0
    for x in range(10, 50000):
        s, n = 0, x
        while n > 0:
            d = n % 10
            n //= 10
            s += fact[d]
        if s == x:
            ans += x

    return ans


print(calc())

    
