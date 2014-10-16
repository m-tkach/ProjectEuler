def gcd(x, y):
    while x * y > 0:
        x, y = y, x%y
    return x + y


def equal(n1, d1, n2, d2):
    g1 = gcd(n1, d1)
    g2 = gcd(n2, d2)
    
    n1 //= g1
    d1 //= g1
    
    n2 //= g2
    d2 //= g2

    return n1 == n2 and d1 == d2


def calc():
    n, d = 1, 1
    
    for a in range(1, 10):
        for b in range(1, 10):
            if a == b:
                continue
            
            for c in range(1, 10):
                if b == c:
                    continue
                
                x = 10 * a + b
                y = 10 * b + c
                if equal(a, c, x, y):
                    n *= a
                    d *= c
                    
    g = gcd(n, d)
    return d // g


print(calc())
    
    
    
    
