N = 1001


def calc():
    ans = 1
    last = 1
    
    for n in range(3, N + 1, 2):
        d = n - 1
        for i in range(4):
            last += d
            ans += last
    
    return ans


print(calc())
        
