def calc():
    ans_list = []
    x = 4
    while True:
        d, n, divs = 2, x, 0
        while d * d <= n:
            if n % d == 0:
                divs += 1
                while n % d == 0:
                    n //= d
            d += 1
        if n > 1:
            divs += 1
        
        if divs == 4:
            ans_list.append(x)
        else:
            ans_list = []

        if len(ans_list) == 4:
            return ans_list[0]
        x += 1
        
           
print(calc())
