MOD = int(10**6)
    

def calc():
    ans = [1, ]
    n = 1
    
    while True:
        ans.append(0)
        i, d = 0, 1
        
        while d <= n:
            sign = 1 if i % 4 < 2 else -1
            ans[n] += sign * ans[n - d]
            ans[n] %= MOD

            i += 1
            j = (i // 2 + 1) if i % 2 == 0 else -(i // 2 + 1)
            d = j * (3 * j - 1) // 2

        if ans[n] == 0:
            return n
        
        n += 1
    
    return None


print(calc())
